import datetime

from peewee import *
from playhouse.pool import MySQLDatabase
from playhouse.shortcuts import RetryOperationalError

from config import config


class RetryMysqlDatabase(RetryOperationalError, MySQLDatabase):
    def __init__(self, database, **kwargs):
        super(MySQLDatabase, self).__init__(database, **kwargs)

    def sequence_exists(self, seq):
        pass


db = RetryMysqlDatabase(
    database=config.DB_NAME, host=config.DB_HOST,
    user=config.DB_USER, passwd=config.DB_PASSWORD, port=config.DB_PORT,
)


class BaseModel(Model):
    """A base model will use MySQL database"""
    is_deleted = BooleanField(verbose_name=u'是否删除', default=False)
    create_time = DateTimeField(verbose_name=u'创建时间', default=datetime.datetime.utcnow)
    update_time = DateTimeField(verbose_name=u'更新时间', default=datetime.datetime.utcnow)
    creator = CharField(verbose_name=u'创建者', null=True)
    updator = CharField(verbose_name=u'更新者', null=True)

    class Meta:
        database = db


class Tenant(BaseModel):
    name = CharField(verbose_name=u'租户名称', unique=True)
    ad_server_uri = CharField(verbose_name=u'租户AD服务地址', null=True)
    ad_bind_dn = CharField(verbose_name=u'租户AD服务DN', null=True)
    admin_ad = CharField(verbose_name=u'租户管理员DN', null=True)
    admin_password = CharField(verbose_name=u'租户管理员密码', null=True)


class System(BaseModel):
    tenant = ForeignKeyField(Tenant, related_name='tenant_systems')
    name = CharField(verbose_name=u'系统名称', unique=True)
    alias = CharField(verbose_name=u'系统别名', null=True)
    desc = CharField(verbose_name=u'系统描述', null=True)


class Role(BaseModel):
    code = CharField(verbose_name=u'角色编码', unique=True)
    desc = CharField(verbose_name=u'角色描述', null=True)


class User(BaseModel):
    tenant = ForeignKeyField(Tenant, related_name='tenant_users')
    username = CharField(verbose_name=u'AD账号', unique=True)
    name = CharField(verbose_name=u'姓名', null=True)
    email = CharField(verbose_name=u'邮箱', null=True)
    phone = CharField(verbose_name=u'联系电话', null=True)
    date_joined = DateTimeField(default=datetime.datetime.utcnow, null=True)
    last_login = DateTimeField(default=datetime.datetime.utcnow, null=True)


class UserRole(BaseModel):
    user = ForeignKeyField(User, related_name='user_user_roles')
    role = ForeignKeyField(Role, related_name='role_user_roles')


class SystemUser(BaseModel):
    system = ForeignKeyField(System, related_name='system_users')
    user = ForeignKeyField(User, related_name='user_systems')
    role = CharField(verbose_name=u'角色', null=True)


class DeployStatus(BaseModel):
    code = CharField(verbose_name=u'上线流程状态码', unique=True)
    desc = CharField(verbose_name=u'上线流程状态描述', null=True)


class DeployInstance(BaseModel):
    system = CharField(verbose_name=u'上线系统')
    version = CharField(verbose_name=u'上线版本号')
    db_type = CharField(verbose_name=u'数据库类型', null=True)
    db_config = CharField(verbose_name=u'数据库IP，Port', null=True)
    db_sql = TextField(verbose_name=u'数据库SQL', null=True)
    cc = CharField(verbose_name=u'抄送邮件组', null=True)
    dev = CharField(verbose_name=u'开发')
    qa = CharField(verbose_name=u'测试')
    ops = CharField(verbose_name=u'运维')
    approver = CharField(verbose_name=u'审批者')
    dba = CharField(verbose_name=u'DBA')
    pm = CharField(verbose_name=u'产品经理')
    operate_dev = CharField(verbose_name=u'操作者-开发', null=True)
    operate_qa = CharField(verbose_name=u'操作者-测试', null=True)
    operate_ops = CharField(verbose_name=u'操作者-运维', null=True)
    operate_approver = CharField(verbose_name=u'操作者-审批者', null=True)
    operate_dba = CharField(verbose_name=u'操作者-DBA', null=True)
    operate_pm = CharField(verbose_name=u'操作者-产品经理', null=True)
    plan_time = DateTimeField(verbose_name=u'预计上线时间')
    content = TextField(verbose_name=u'上线内容')
    approver_time = DateTimeField(verbose_name=u'审批者审批', null=True)
    qa_time = DateTimeField(verbose_name=u'测试审批', null=True)
    ops_time = DateTimeField(verbose_name=u'运维审批', null=True)
    dev_time = DateTimeField(verbose_name=u'开发验收通过', null=True)
    dba_time = DateTimeField(verbose_name=u'DBA通过', null=True)
    pm_time = DateTimeField(verbose_name=u'PM验收通过', null=True)
    status = IntegerField(verbose_name=u'流程状态')
    bak_status = IntegerField(verbose_name=u'流程状态备份，保存正常通过状态')
    have_sql = BooleanField(verbose_name=u'是否有数据变更', default=False)


class DeployInstanceUser(BaseModel):
    deploy = ForeignKeyField(DeployInstance, related_name='deploy_users')
    user = ForeignKeyField(User, related_name='user_deploys')
    role = CharField(verbose_name=u'角色', null=True)


class DeployInstanceComment(BaseModel):
    deploy = ForeignKeyField(DeployInstance, related_name='deploy_comments')
    content = TextField(verbose_name=u'评论内容')


class DeployInstanceFile(BaseModel):
    deploy = ForeignKeyField(DeployInstance, related_name='deploy_files')
    access_url = TextField(verbose_name=u'下载地址', null=True)
    file_name = CharField(verbose_name=u'文件名', null=True)


class ChangeStatus(BaseModel):
    code = CharField(verbose_name=u'上线流程状态码', unique=True)
    desc = CharField(verbose_name=u'上线流程状态描述', null=True)


class ChangeInstance(BaseModel):
    system = CharField(verbose_name=u'变更系统')
    change_type = CharField(verbose_name=u'变更类型')
    version = CharField(verbose_name=u'变更版本号')
    db_type = CharField(verbose_name=u'数据库类型', null=True)
    db_config = CharField(verbose_name=u'数据库IP，Port', null=True)
    db_sql = TextField(verbose_name=u'数据库SQL', null=True)
    cc = CharField(verbose_name=u'抄送邮件组', null=True)
    plan_time = DateTimeField(verbose_name=u'预计变更时间')
    problem_desc = TextField(verbose_name=u'线上问题描述')
    content_desc = TextField(verbose_name=u'变更内容描述')
    risk_desc = TextField(verbose_name=u'变更执行风险描述')
    dev = CharField(verbose_name=u'开发')
    qa = CharField(verbose_name=u'测试')
    ops = CharField(verbose_name=u'运维')
    approver = CharField(verbose_name=u'审批者')
    dba = CharField(verbose_name=u'DBA')
    pm = CharField(verbose_name=u'产品经理')
    operate_dev = CharField(verbose_name=u'操作者-开发', null=True)
    operate_qa = CharField(verbose_name=u'操作者-测试', null=True)
    operate_ops = CharField(verbose_name=u'操作者-运维', null=True)
    operate_approver = CharField(verbose_name=u'操作者-审批者', null=True)
    operate_dba = CharField(verbose_name=u'操作者-DBA', null=True)
    operate_pm = CharField(verbose_name=u'操作者-产品经理', null=True)
    approver_time = DateTimeField(verbose_name=u'审批者审批', null=True)
    qa_time = DateTimeField(verbose_name=u'测试审批', null=True)
    ops_time = DateTimeField(verbose_name=u'运维审批', null=True)
    dev_time = DateTimeField(verbose_name=u'开发验收通过', null=True)
    dba_time = DateTimeField(verbose_name=u'DBA通过', null=True)
    pm_time = DateTimeField(verbose_name=u'PM验收通过', null=True)
    status = IntegerField(verbose_name=u'流程状态')
    bak_status = IntegerField(verbose_name=u'流程状态备份，保存正常通过状态')
    have_sql = BooleanField(verbose_name=u'是否有数据变更', default=False)


class ChangeInstanceUser(BaseModel):
    change = ForeignKeyField(ChangeInstance, related_name='change_users')
    user = ForeignKeyField(User, related_name='user_changes')
    role = CharField(verbose_name=u'角色', null=True)


class ChangeInstanceComment(BaseModel):
    change = ForeignKeyField(ChangeInstance, related_name='change_comments')
    content = TextField(verbose_name=u'评论内容')


class ChangeInstanceFile(BaseModel):
    change = ForeignKeyField(ChangeInstance, related_name='change_files')
    access_url = TextField(verbose_name=u'下载地址', null=True)
    file_name = CharField(verbose_name=u'文件名', null=True)
