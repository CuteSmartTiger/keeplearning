# coding=utf8
import datetime
import uuid

from sanic.views import HTTPMethodView
from sanic import response

from base.mixin import login_required, Auth, PaginateMixin
from base import tools
from core import models, serialize, mail
from config import config
from base.cos import Cos
import const


class LoginView(HTTPMethodView):
    async def post(self, request):
        data = request["POST"]
        tenant = data.get("tenant")
        username = data.get("username")
        password = data.get("password")
        if not username or not password or not tenant:
            return response.json({"status": const.FAIL_STATUS, "msg": "主体、账户名和密码不能为空"})
        is_authorized, token, msg = Auth.authenticate(tenant, username, password)
        if is_authorized:
            return response.json(
                {"status": const.SUCCESS_STATUS, "msg": msg,
                 "data": dict(token=token, username=username, tenant=tenant)})
        else:
            return response.json({"status": const.FAIL_STATUS, "msg": msg})


class TenantView(HTTPMethodView):
    async def get(self, request):
        tenants = models.Tenant.select().where(models.Tenant.is_deleted == 0)
        tenant_schema = serialize.TenantSchema()
        data = dict(tenants=tenant_schema.dump(tenants, many=True).data)
        return response.json({"status": const.SUCCESS_STATUS, "data": data, "msg": "获取成功"})


class UserView(HTTPMethodView):
    @login_required
    async def get(self, request):
        data = request["GET"]
        roles = data.get("roles")
        roles = roles.split(',') if roles else None
        username = request['username']
        user = models.User.get(models.User.username == username)
        user_tenant = user.tenant
        user_schema = serialize.UserSchema()
        if roles and isinstance(roles, list):
            data = {}
            for role_code in roles:
                try:
                    role = models.Role.get(models.Role.code == role_code)
                    role_users = []
                    for user_role in role.role_user_roles:
                        if user_role.user.tenant == user_tenant:
                            role_users.append(user_role.user)
                    data[role_code] = user_schema.dump(role_users, many=True).data
                except models.Role.DoesNotExist:
                    pass
        else:
            users = models.User.select().where(
                (models.User.is_deleted == 0) &
                (models.User.tenant == user.tenant)
            ).order_by(models.User.id.desc())
            data = dict(users=user_schema.dump(users, many=True).data)
            data['user_roles'] = {}
            for user in users:
                user_roles = user.user_user_roles
                roles = [user_role.role.code for user_role in user_roles]
                data['user_roles'][user.username] = roles
        return response.json({"status": const.SUCCESS_STATUS, "data": data, "msg": "获取成功"})

    @login_required
    async def put(self, request):
        data = request["PUT"]
        update_username = data.get("username")
        update_name = data.get("name")
        update_phone = data.get("phone")
        update_email = data.get("email")
        update_roles = data.get("role_list")
        username = request['username']
        user = models.User.get(models.User.username == username)
        # 判断角色、权限
        user_roles = user.user_user_roles
        roles = [user_role.role.code for user_role in user_roles]
        # 如果是admin
        if const.ADMIN not in roles:
            return response.json({"status": const.FAIL_STATUS, "msg": "没有权限"})
        try:
            update_user = models.User.get(models.User.username == update_username)
            update_user.name = update_name
            update_user.phone = update_phone
            update_user.email = update_email
            update_user.updator = user.username
            update_user.update_time = tools.utc_now()
            update_user.save()
            if update_roles and isinstance(update_roles, list):
                src_user_roles = update_user.user_user_roles
                src_roles = [user_role.role.code for user_role in src_user_roles]
                src_roles, update_roles = set(src_roles), set(update_roles)
                need_add_codes = update_roles.difference(src_roles)
                need_delete_codes = src_roles.difference(update_roles)
                for need_add_code in need_add_codes:
                    try:
                        need_role = models.Role.get(models.Role.code == need_add_code)
                        user_role = models.UserRole()
                        user_role.user = update_user
                        user_role.role = need_role
                        user_role.save()
                    except models.Role.DoesNotExist:
                        pass
                for need_delete_code in need_delete_codes:
                    try:
                        need_role = models.Role.get(models.Role.code == need_delete_code)
                        models.UserRole.delete().where(
                            (models.UserRole.user == update_user) &
                            (models.UserRole.role == need_role)
                        ).execute()
                    except models.Role.DoesNotExist:
                        pass
            return response.json({"status": const.SUCCESS_STATUS, "msg": "更新成功"})
        except models.System.DoesNotExist:
            return response.json({"status": const.FAIL_STATUS, "msg": "用户不存在"})


class SystemView(HTTPMethodView):
    @login_required
    async def get(self, request):
        username = request['username']
        user = models.User.get(models.User.username == username)
        systems = models.System.select().where(
            (models.System.is_deleted == 0) &
            (models.System.tenant == user.tenant)
        ).order_by(models.System.id.desc())
        system_schema = serialize.SystemSchema()
        data = dict(systems=system_schema.dump(systems, many=True).data)
        data['system_users'] = {}
        for system in systems:
            system_users = system.system_users
            user_roles = [[system_user.role, system_user.user.username, system_user.user.name] for system_user in
                          system_users]
            data['system_users'][system.name] = user_roles
        return response.json({"status": const.SUCCESS_STATUS, "data": data, "msg": "获取成功"})

    @login_required
    async def post(self, request):
        data = request["POST"]
        system_name = data.get("system_name")
        system_alias = data.get("system_alias")
        system_desc = data.get("system_desc")
        username = request['username']
        user = models.User.get(models.User.username == username)
        # 判断角色、权限
        user_roles = user.user_user_roles
        roles = [user_role.role.code for user_role in user_roles]
        # 如果是admin可以看到所有的上线流程
        if const.ADMIN not in roles:
            return response.json({"status": const.FAIL_STATUS, "msg": "没有权限"})
        try:
            models.System.get(models.System.name == system_name)
            return response.json({"status": const.FAIL_STATUS, "msg": "系统名不能重复"})
        except models.System.DoesNotExist:
            system = models.System()
            system.tenant = user.tenant
            system.name = system_name
            system.alias = system_alias
            system.desc = system_desc
            system.creator = user.username
            system.save()
            return response.json({"status": const.SUCCESS_STATUS, "msg": "添加成功"})

    @login_required
    async def put(self, request):
        data = request["PUT"]
        system_id = data.get("system_id")
        dev = data.get("dev")
        qa = data.get("qa")
        ops = data.get("ops")
        approver = data.get("approver")
        dba = data.get("dba")
        pm = data.get("pm")
        username = request['username']
        user = models.User.get(models.User.username == username)
        # 判断角色、权限
        user_roles = user.user_user_roles
        roles = [user_role.role.code for user_role in user_roles]
        # 如果是admin操作
        if const.ADMIN not in roles:
            return response.json({"status": const.FAIL_STATUS, "msg": "没有权限"})
        system = models.System.get(models.System.id == system_id)
        models.SystemUser.delete().where(
            models.SystemUser.system == system).execute()
        # 将系统相关的人员存储
        relations = [{const.DEV: dev}, {const.OPS: ops}, {const.QA: qa}, {const.APPROVER: approver}, {const.DBA: dba},
                     {const.PM: pm}]
        for relation in relations:
            k = list(relation.keys())[0]
            v = list(relation.values())[0]
            users = v.split(',')
            for user in users:
                try:
                    system_user_role = models.SystemUser()
                    system_user_role.system = system
                    system_user_role.user = models.User.get(models.User.username == user)
                    system_user_role.role = k
                    system_user_role.save()
                    print(system.name, user.username, k)
                except Exception:
                    pass
        return response.json({"status": const.SUCCESS_STATUS, "msg": "更新成功"})


class DeployView(HTTPMethodView):
    @login_required
    async def post(self, request):
        data = request["POST"]
        system = data.get("system")
        dev = data.get("dev")
        qa = data.get("qa")
        ops = data.get("ops")
        dba = data.get("dba")
        pm = data.get("pm")
        approver = data.get("approver")
        plan_date = data.get("plan_date")
        plan_time = data.get("plan_time")
        content = data.get("content")
        version = data.get("version")
        db_type = data.get("db_type")
        db_config = data.get("db_config")
        db_sql = data.get("db_sql")
        cc = data.get("cc")
        upload_files = data.get("upload_files")
        have_sql = data.get("have_sql")
        username = request['username']
        plan_time = '{0} {1}'.format(plan_date, plan_time)
        deploy = models.DeployInstance()
        deploy.system = system
        deploy.dev = dev
        deploy.qa = qa
        deploy.ops = ops
        deploy.approver = approver
        deploy.dba = dba
        deploy.pm = pm
        deploy.plan_time = tools.str2datetime(plan_time, _utc=True)
        deploy.content = content
        deploy.version = version
        deploy.db_type = db_type
        deploy.db_config = db_config
        deploy.db_sql = db_sql
        deploy.cc = cc
        deploy.creator = username
        deploy.updator = username
        deploy.status = const.WAIT_QA
        deploy.bak_status = const.WAIT_QA
        deploy.have_sql = have_sql
        deploy.save()
        # 上传文件存储
        for upload_file in upload_files:
            deploy_file = models.DeployInstanceFile()
            deploy_file.deploy = deploy
            deploy_file.access_url = upload_file.get('access_url')
            deploy_file.file_name = upload_file.get('file_name')
            deploy_file.save()
        # 发送邮件
        mail.deploy_mail(deploy)
        # 将流程相关的人员存储
        relations = [{'CREATOR': username}, {const.DEV: dev}, {const.OPS: ops}, {const.QA: qa},
                     {const.APPROVER: approver}, {const.DBA: dba}, {const.PM: pm}]
        for relation in relations:
            k = list(relation.keys())[0]
            v = list(relation.values())[0]
            users = v.split(',')
            for user in users:
                try:
                    deploy_user_role = models.DeployInstanceUser()
                    deploy_user_role.deploy = deploy
                    deploy_user_role.user = models.User.get(models.User.username == user)
                    deploy_user_role.role = k
                    deploy_user_role.save()
                except Exception:
                    pass
        return response.json({"status": const.SUCCESS_STATUS, "msg": "创建成功"})

    @login_required
    async def get(self, request):
        data = request["GET"]
        username = request['username']
        user = models.User.get(models.User.username == username)
        user_tenant = user.tenant
        ID = data.get("ID", None)
        close = data.get("close", None)
        not_deleted = (models.DeployInstance.is_deleted == 0)
        deploy_schema = serialize.DeploySchema()
        if ID:
            deploy = models.DeployInstance.get(
                not_deleted & (models.DeployInstance.id == ID))
            deploy_comment_schema = serialize.DeployCommentSchema()
            deploy_comments = deploy.deploy_comments
            deploy_file_schema = serialize.DeployFileSchema()
            deploy_files = deploy.deploy_files
            data = dict(deploy=deploy_schema.dump(deploy).data,
                        deploy_comments=deploy_comment_schema.dump(deploy_comments, many=True).data,
                        deploy_files=deploy_file_schema.dump(deploy_files, many=True).data)
        else:
            # 判断类型
            todo_list = [const.WAIT_APPROVE, const.WAIT_QA, const.WAIT_DEV, const.WAIT_OPS]
            history_list = [const.DONE, const.CANCEL, const.REJECT]
            if close == const.RELATION:
                q = (models.DeployInstance.status.in_(todo_list))
            elif close == const.HISTORY:
                q = (models.DeployInstance.status.in_(history_list))
            else:
                q = not_deleted
            # 判断角色、权限
            user_roles = user.user_user_roles
            roles = [user_role.role.code for user_role in user_roles]
            # 如果是admin可以看到所有的上线流程
            if const.ADMIN in roles:
                tenant_systems = user_tenant.tenant_systems
                tenant_system_names = [tenant_system.name for tenant_system in tenant_systems]
                p = (models.DeployInstance.system.in_(tenant_system_names))
                deploys = models.DeployInstance.select().where(not_deleted & q & p).order_by(
                    models.DeployInstance.id.desc())
            else:
                user_deploy_roles = user.user_deploys
                deploy_ids = [user_deploy_role.deploy.id for user_deploy_role in user_deploy_roles]
                p = (models.DeployInstance.id.in_(deploy_ids))
                deploys = models.DeployInstance.select().where(not_deleted & q & p).order_by(
                    models.DeployInstance.id.desc())
            data = dict(deploys=deploy_schema.dump(deploys, many=True).data)
        return response.json({"status": const.SUCCESS_STATUS, "data": data, "msg": "获取成功"})

    @login_required
    async def put(self, request):
        data = request["PUT"]
        username = request['username']
        user = models.User.get(models.User.username == username)
        ID = data.get("ID", None)
        action = data.get("action", None)
        not_deleted = (models.DeployInstance.is_deleted == 0)
        deploy = models.DeployInstance.get(
            not_deleted & (models.DeployInstance.id == ID))
        deploy.updator = username
        deploy.update_time = tools.utc_now()
        # DBA 和 OPS 分开确认(判断是否有SQL)
        ops_done = True
        # 判断角色、权限, 如果是admin可以看到所有的上线流程
        user_roles = user.user_user_roles
        roles = [user_role.role.code for user_role in user_roles]
        is_admin = const.ADMIN in roles
        is_approver = is_admin or username in deploy.approver.split(',')
        is_qa = is_admin or username in deploy.qa.split(',')
        is_ops = is_admin or username in deploy.ops.split(',')
        is_dba = is_admin or username in deploy.dba.split(',')
        is_dev = is_admin or username in deploy.dev.split(',')
        is_pm = is_admin or username in deploy.pm.split(',')
        # 根据不同的动作执行不同的操作和判断权限
        if action == const.ACTION_APPROVE:
            if deploy.status == const.WAIT_APPROVE and is_approver:
                deploy.approver_time = tools.utc_now()
                deploy.operate_approver = username
            elif deploy.status == const.WAIT_QA and is_qa:
                deploy.qa_time = tools.utc_now()
                deploy.operate_qa = username
            # OPS 确认
            elif deploy.status == const.WAIT_OPS and is_ops and not deploy.operate_ops:
                deploy.ops_time = tools.utc_now()
                deploy.operate_ops = username
            # DBA 和 OPS 分开确认
            elif deploy.status == const.WAIT_OPS and is_dba and not deploy.operate_dba and deploy.have_sql:
                deploy.dba_time = tools.utc_now()
                deploy.operate_dba = username
            elif deploy.status == const.WAIT_DEV and is_dev:
                deploy.dev_time = tools.utc_now()
                deploy.operate_dev = username
            elif deploy.status == const.WAIT_DEV and is_pm:
                deploy.pm_time = tools.utc_now()
                deploy.operate_pm = username
            else:
                return response.json({"status": const.FAIL_STATUS, "msg": "没有权限"})
            if deploy.have_sql and deploy.status == const.WAIT_OPS and (
                        not deploy.operate_ops or not deploy.operate_dba):
                ops_done = False
            # 判断有SQL的情况下是否OPS和DBA都操作完成
            if ops_done:
                deploy.status += 1
                deploy.bak_status += 1
                deploy.save()
            else:
                deploy.save()
            # 发送邮件
            mail.deploy_mail(deploy)
        elif action == const.ACTION_CANCEL:
            deploy.status = const.CANCEL
            deploy.update_time = tools.utc_now()
            deploy.save()
        elif action == const.ACTION_REJECT:
            if username in deploy.approver.split(','):
                deploy.status = const.REJECT
                deploy.update_time = tools.utc_now()
                deploy.save()
            else:
                return response.json({"status": const.FAIL_STATUS, "msg": "没有权限"})
        else:
            pass
        return response.json({"status": const.SUCCESS_STATUS, "msg": "执行成功"})


class DeployCommentView(HTTPMethodView):
    @login_required
    async def post(self, request):
        data = request["POST"]
        username = request['username']
        ID = data.get("ID", None)
        comment = data.get("comment", None)
        not_deleted = (models.DeployInstance.is_deleted == 0)
        if ID:
            deploy = models.DeployInstance.get(
                not_deleted & (models.DeployInstance.id == ID))
            deploy_comment = models.DeployInstanceComment()
            deploy_comment.deploy = deploy
            deploy_comment.creator = username
            deploy_comment.updator = username
            deploy_comment.content = comment
            deploy_comment.save()
        return response.json({"status": const.SUCCESS_STATUS, "msg": "添加成功"})


class DeployUploadView(HTTPMethodView):
    @login_required
    async def post(self, request):
        data = request.files
        post_data = request.form
        upload_file = data.get('file')
        deploy_id = post_data.get('deploy_id')
        file_name = upload_file.name
        file_body = upload_file.body
        file_name = '{0}_{1}'.format(uuid.uuid1(), file_name)
        cos = Cos(app_id=config.TC_ID,
                  secret_id=config.TC_SECRET_ID,
                  secret_key=config.TC_SECRET_KEY,
                  region=config.TC_REGION)
        bucket = cos.get_bucket(config.TC_BUCKET)
        data = bucket.upload_simple_file(file_body=file_body,
                                         file_name=file_name)
        if data and isinstance(eval(data), dict):
            access_url = eval(data).get("access_url")
            data = dict(access_url=access_url, file_name=file_name)
            if deploy_id:
                not_deleted = (models.DeployInstance.is_deleted == 0)
                deploy = models.DeployInstance.get(
                    not_deleted & (models.DeployInstance.id == deploy_id))
                # 上传文件存储
                deploy_file = models.DeployInstanceFile()
                deploy_file.deploy = deploy
                deploy_file.access_url = access_url
                deploy_file.file_name = file_name
                deploy_file.save()
            return response.json({"status": const.SUCCESS_STATUS, "data": data, "msg": "上传成功"})
        else:
            return response.json({"status": const.FAIL_STATUS, "msg": "上传失败"})

    @login_required
    async def put(self, request):
        data = request["PUT"]
        file_name = data.get('file_name')
        ID = data.get('ID')
        cos = Cos(app_id=config.TC_ID,
                  secret_id=config.TC_SECRET_ID,
                  secret_key=config.TC_SECRET_KEY,
                  region=config.TC_REGION)
        bucket = cos.get_bucket(config.TC_BUCKET)
        _ = bucket.delete_file(dest_fileid=file_name)
        if ID:
            # 删除存储文件
            models.DeployInstanceFile.delete().where(
                models.DeployInstanceFile.id == ID).execute()
        return response.json({"status": const.SUCCESS_STATUS, "msg": "删除成功"})


class DeployTodoView(HTTPMethodView):
    @login_required
    async def get(self, request):
        username = request['username']
        user = models.User.get(models.User.username == username)
        not_deleted = (models.DeployInstance.is_deleted == 0)
        user_deploy_roles = user.user_deploys
        deploy_ids = [user_deploy_role.deploy.id for user_deploy_role in user_deploy_roles]
        p = (models.DeployInstance.id.in_(deploy_ids))
        todo_list = [const.WAIT_APPROVE, const.WAIT_QA, const.WAIT_DEV, const.WAIT_OPS]
        q = (models.DeployInstance.status.in_(todo_list))
        deploys = models.DeployInstance.select().where(not_deleted & q & p).order_by(
            models.DeployInstance.id.desc())
        deploy_todos = []
        for deploy in deploys:
            if deploy.status == const.WAIT_APPROVE and username in deploy.approver.split(','):
                deploy_todos.append(deploy)
            elif deploy.status == const.WAIT_QA and username in deploy.qa.split(','):
                deploy_todos.append(deploy)
            elif deploy.status == const.WAIT_OPS and username in deploy.ops.split(','):
                deploy_todos.append(deploy)
            elif deploy.status == const.WAIT_DEV and username in deploy.dev.split(','):
                deploy_todos.append(deploy)
            else:
                pass
        deploy_schema = serialize.DeploySchema()
        data = dict(deploys=deploy_schema.dump(deploy_todos, many=True).data)
        return response.json({"status": const.SUCCESS_STATUS, "data": data, "msg": "获取成功"})


class ChangeUploadView(HTTPMethodView):
    @login_required
    async def post(self, request):
        data = request.files
        post_data = request.form
        upload_file = data.get('file')
        change_id = post_data.get('change_id')
        file_name = upload_file.name
        file_body = upload_file.body
        file_name = '{0}_{1}'.format(uuid.uuid1(), file_name)
        cos = Cos(app_id=config.TC_ID,
                  secret_id=config.TC_SECRET_ID,
                  secret_key=config.TC_SECRET_KEY,
                  region=config.TC_REGION)
        bucket = cos.get_bucket(config.TC_BUCKET)
        data = bucket.upload_simple_file(file_body=file_body,
                                         file_name=file_name)
        if data and isinstance(eval(data), dict):
            access_url = eval(data).get("access_url")
            data = dict(access_url=access_url, file_name=file_name)
            if change_id:
                not_deleted = (models.ChangeInstance.is_deleted == 0)
                change = models.ChangeInstance.get(
                    not_deleted & (models.ChangeInstance.id == change_id))
                # 上传文件存储
                change_file = models.ChangeInstanceFile()
                change_file.change = change
                change_file.access_url = access_url
                change_file.file_name = file_name
                change_file.save()
            return response.json({"status": const.SUCCESS_STATUS, "data": data, "msg": "上传成功"})
        else:
            return response.json({"status": const.FAIL_STATUS, "msg": "上传失败"})

    @login_required
    async def put(self, request):
        data = request["PUT"]
        file_name = data.get('file_name')
        ID = data.get('ID')
        cos = Cos(app_id=config.TC_ID,
                  secret_id=config.TC_SECRET_ID,
                  secret_key=config.TC_SECRET_KEY,
                  region=config.TC_REGION)
        bucket = cos.get_bucket(config.TC_BUCKET)
        _ = bucket.delete_file(dest_fileid=file_name)
        if ID:
            # 删除存储文件
            models.ChangeInstanceFile.delete().where(
                models.ChangeInstanceFile.id == ID).execute()
        return response.json({"status": const.SUCCESS_STATUS, "msg": "删除成功"})


class ChangeView(HTTPMethodView):
    @login_required
    async def post(self, request):
        data = request["POST"]
        system = data.get("system")
        change_type = data.get("change_type")
        dev = data.get("dev")
        qa = data.get("qa")
        ops = data.get("ops")
        dba = data.get("dba")
        pm = data.get("pm")
        approver = data.get("approver")
        plan_date = data.get("plan_date")
        plan_time = data.get("plan_time")
        problem_desc = data.get("problem_desc")
        content_desc = data.get("content_desc")
        risk_desc = data.get("risk_desc")
        version = data.get("version")
        db_type = data.get("db_type")
        db_config = data.get("db_config")
        db_sql = data.get("db_sql")
        have_sql = data.get("have_sql")
        cc = data.get("cc")
        upload_files = data.get("upload_files")
        username = request['username']
        plan_time = '{0} {1}'.format(plan_date, plan_time)
        change = models.ChangeInstance()
        change.system = system
        change.change_type = change_type
        change.dev = dev
        change.qa = qa
        change.ops = ops
        change.dba = dba
        change.pm = pm
        change.approver = approver
        change.plan_time = tools.str2datetime(plan_time, _utc=True)
        change.problem_desc = problem_desc
        change.content_desc = content_desc
        change.risk_desc = risk_desc
        change.version = version
        change.db_type = db_type
        change.db_config = db_config
        change.db_sql = db_sql
        change.cc = cc
        change.creator = username
        change.updator = username
        change.status = const.WAIT_QA
        change.bak_status = const.WAIT_QA
        change.have_sql = have_sql
        change.save()
        # 上传文件存储
        for upload_file in upload_files:
            change_file = models.ChangeInstanceFile()
            change_file.change = change
            change_file.access_url = upload_file.get('access_url')
            change_file.file_name = upload_file.get('file_name')
            change_file.save()
        # # 发送邮件
        mail.change_mail(change)
        # 将流程相关的人员存储
        relations = [{'CREATOR': username}, {const.DEV: dev}, {const.OPS: ops}, {const.QA: qa},
                     {const.APPROVER: approver}, {const.DBA: dba}, {const.PM: pm}]
        for relation in relations:
            k = list(relation.keys())[0]
            v = list(relation.values())[0]
            users = v.split(',')
            for user in users:
                try:
                    change_user_role = models.ChangeInstanceUser()
                    change_user_role.change = change
                    change_user_role.user = models.User.get(models.User.username == user)
                    change_user_role.role = k
                    change_user_role.save()
                except Exception:
                    pass
        return response.json({"status": const.SUCCESS_STATUS, "msg": "创建成功"})

    @login_required
    async def get(self, request):
        data = request["GET"]
        username = request['username']
        user = models.User.get(models.User.username == username)
        user_tenant = user.tenant
        ID = data.get("ID", None)
        close = data.get("close", None)
        not_deleted = (models.ChangeInstance.is_deleted == 0)
        change_schema = serialize.ChangeSchema()
        if ID:
            change = models.ChangeInstance.get(
                not_deleted & (models.ChangeInstance.id == ID))
            change_comment_schema = serialize.ChangeCommentSchema()
            change_comments = change.change_comments
            change_file_schema = serialize.ChangeFileSchema()
            change_files = change.change_files
            data = dict(change=change_schema.dump(change).data,
                        change_comments=change_comment_schema.dump(change_comments, many=True).data,
                        change_files=change_file_schema.dump(change_files, many=True).data)
        else:
            # 判断类型
            todo_list = [const.WAIT_APPROVE, const.WAIT_QA, const.WAIT_DEV, const.WAIT_OPS]
            history_list = [const.DONE, const.CANCEL, const.REJECT]
            if close == const.RELATION:
                q = (models.ChangeInstance.status.in_(todo_list))
            elif close == const.HISTORY:
                q = (models.ChangeInstance.status.in_(history_list))
            else:
                q = not_deleted
            # 判断角色、权限
            user_roles = user.user_user_roles
            roles = [user_role.role.code for user_role in user_roles]
            # 如果是admin可以看到所有的上线流程
            if const.ADMIN in roles:
                tenant_systems = user_tenant.tenant_systems
                tenant_system_names = [tenant_system.name for tenant_system in tenant_systems]
                p = (models.ChangeInstance.system.in_(tenant_system_names))
                changes = models.ChangeInstance.select().where(not_deleted & q & p).order_by(
                    models.ChangeInstance.id.desc())
            else:
                user_change_roles = user.user_changes
                change_ids = [user_change_role.change.id for user_change_role in user_change_roles]
                p = (models.ChangeInstance.id.in_(change_ids))
                changes = models.ChangeInstance.select().where(not_deleted & q & p).order_by(
                    models.ChangeInstance.id.desc())
            data = dict(changes=change_schema.dump(changes, many=True).data)
        return response.json({"status": const.SUCCESS_STATUS, "data": data, "msg": "获取成功"})

    @login_required
    async def put(self, request):
        data = request["PUT"]
        username = request['username']
        user = models.User.get(models.User.username == username)
        ID = data.get("ID", None)
        action = data.get("action", None)
        not_deleted = (models.ChangeInstance.is_deleted == 0)
        change = models.ChangeInstance.get(
            not_deleted & (models.ChangeInstance.id == ID))
        change.updator = username
        change.update_time = tools.utc_now()
        # DBA 和 OPS 分开确认(判断是否有SQL)
        ops_done = True
        # 判断角色、权限, 如果是admin可以看到所有的上线流程
        user_roles = user.user_user_roles
        roles = [user_role.role.code for user_role in user_roles]
        is_admin = const.ADMIN in roles
        is_approver = is_admin or username in change.approver.split(',')
        is_qa = is_admin or username in change.qa.split(',')
        is_ops = is_admin or username in change.ops.split(',')
        is_dba = is_admin or username in change.dba.split(',')
        is_dev = is_admin or username in change.dev.split(',')
        is_pm = is_admin or username in change.pm.split(',')
        # 根据不同的动作执行不同的操作和判断权限
        if action == const.ACTION_APPROVE:
            if change.status == const.WAIT_APPROVE and is_approver:
                change.approver_time = tools.utc_now()
                change.operate_approver = username
            elif change.status == const.WAIT_QA and is_qa:
                change.qa_time = tools.utc_now()
                change.operate_qa = username
            elif change.status == const.WAIT_DEV and is_dev:
                change.dev_time = tools.utc_now()
                change.operate_dev = username
            elif change.status == const.WAIT_DEV and is_pm:
                change.pm_time = tools.utc_now()
                change.operate_pm = username
            # OPS 确认
            elif change.status == const.WAIT_OPS and is_ops and not change.operate_ops:
                change.ops_time = tools.utc_now()
                change.operate_ops = username
            # DBA 和 OPS 分开确认
            elif change.status == const.WAIT_OPS and is_dba and not change.operate_dba and change.have_sql:
                change.dba_time = tools.utc_now()
                change.operate_dba = username
            else:
                return response.json({"status": const.FAIL_STATUS, "msg": "没有权限"})
            # 判断是否执行结束
            if change.have_sql and change.status == const.WAIT_OPS and (
                        not change.operate_ops or not change.operate_dba):
                ops_done = False
                # 判断有SQL的情况下是否OPS和DBA都操作完成
            if ops_done:
                change.status += 1
                change.bak_status += 1
                change.save()
            else:
                change.save()
            # 发送邮件
            mail.change_mail(change)
        elif action == const.ACTION_CANCEL:
            change.status = const.CANCEL
            change.update_time = tools.utc_now()
            change.save()
        elif action == const.ACTION_REJECT:
            if username in change.approver.split(','):
                change.status = const.REJECT
                change.update_time = tools.utc_now()
                change.save()
            else:
                return response.json({"status": const.FAIL_STATUS, "msg": "没有权限"})
        else:
            pass
        return response.json({"status": const.SUCCESS_STATUS, "msg": "执行成功"})


class ChangeCommentView(HTTPMethodView):
    @login_required
    async def post(self, request):
        data = request["POST"]
        username = request['username']
        ID = data.get("ID", None)
        comment = data.get("comment", None)
        not_deleted = (models.ChangeInstance.is_deleted == 0)
        if ID:
            change = models.ChangeInstance.get(
                not_deleted & (models.ChangeInstance.id == ID))
            change_comment = models.ChangeInstanceComment()
            change_comment.change = change
            change_comment.creator = username
            change_comment.updator = username
            change_comment.content = comment
            change_comment.save()
        return response.json({"status": const.SUCCESS_STATUS, "msg": "添加成功"})


class ChangeTodoView(HTTPMethodView):
    @login_required
    async def get(self, request):
        username = request['username']
        user = models.User.get(models.User.username == username)
        not_deleted = (models.ChangeInstance.is_deleted == 0)
        user_change_roles = user.user_changes
        change_ids = [user_change_role.change.id for user_change_role in user_change_roles]
        p = (models.ChangeInstance.id.in_(change_ids))
        todo_list = [const.WAIT_APPROVE, const.WAIT_QA, const.WAIT_DEV, const.WAIT_OPS]
        q = (models.ChangeInstance.status.in_(todo_list))
        changes = models.ChangeInstance.select().where(not_deleted & q & p).order_by(
            models.ChangeInstance.id.desc())
        change_todos = []
        for change in changes:
            if change.status == const.WAIT_APPROVE and username in change.approver.split(','):
                change_todos.append(change)
            elif change.status == const.WAIT_QA and username in change.qa.split(','):
                change_todos.append(change)
            elif change.status == const.WAIT_OPS and username in change.ops.split(','):
                change_todos.append(change)
            elif change.status == const.WAIT_DEV and username in change.dev.split(','):
                change_todos.append(change)
            else:
                pass
        change_schema = serialize.ChangeSchema()
        data = dict(changes=change_schema.dump(change_todos, many=True).data)
        return response.json({"status": const.SUCCESS_STATUS, "data": data, "msg": "获取成功"})
