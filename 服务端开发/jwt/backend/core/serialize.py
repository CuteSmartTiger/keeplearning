from marshmallow import Schema, fields, post_load
from core import models


class TenantSchema(Schema):
    ID = fields.Integer(allow_none=True, attribute="id")
    name = fields.String(required=True)

    @post_load
    def make_tenant(self, data):
        return models.Tenant(**data)


class UserSchema(Schema):
    ID = fields.Integer(allow_none=True, attribute="id")
    tenant = fields.Nested(TenantSchema, required=True)
    username = fields.String(required=True)
    name = fields.String(allow_none=True)
    email = fields.String(allow_none=True)
    phone = fields.String(allow_none=True)
    date_joined = fields.DateTime(allow_none=True)
    last_login = fields.DateTime(allow_none=True)

    @post_load
    def make_user(self, data):
        return models.User(**data)


class SystemSchema(Schema):
    ID = fields.Integer(allow_none=True, attribute="id")
    tenant = fields.Nested(TenantSchema, required=True)
    name = fields.String(required=True)
    alias = fields.String(allow_none=True)
    desc = fields.String(allow_none=True)

    @post_load
    def make_system(self, data):
        return models.System(**data)


class DeploySchema(Schema):
    ID = fields.Integer(allow_none=True, attribute="id")
    creator = fields.String(allow_none=True)
    create_time = fields.DateTime(allow_none=True)
    updator = fields.String(allow_none=True)
    update_time = fields.DateTime(allow_none=True)
    system = fields.String(required=True)
    version = fields.String(required=True)
    db_type = fields.String(allow_none=True)
    db_config = fields.String(allow_none=True)
    db_sql = fields.String(allow_none=True)
    cc = fields.String(allow_none=True)
    dev = fields.String(allow_none=True)
    qa = fields.String(allow_none=True)
    ops = fields.String(allow_none=True)
    approver = fields.String(allow_none=True)
    dba = fields.String(allow_none=True)
    pm = fields.String(allow_none=True)
    operate_dev = fields.String(allow_none=True)
    operate_qa = fields.String(allow_none=True)
    operate_ops = fields.String(allow_none=True)
    operate_approver = fields.String(allow_none=True)
    operate_dba = fields.String(allow_none=True)
    operate_pm = fields.String(allow_none=True)
    plan_time = fields.DateTime(allow_none=True)
    content = fields.String(allow_none=True)
    approver_time = fields.DateTime(allow_none=True)
    qa_time = fields.DateTime(allow_none=True)
    ops_time = fields.DateTime(allow_none=True)
    dev_time = fields.DateTime(allow_none=True)
    dba_time = fields.DateTime(allow_none=True)
    pm_time = fields.DateTime(allow_none=True)
    status = fields.Integer(allow_none=True)
    bak_status = fields.Integer(allow_none=True)

    @post_load
    def make_deploy(self, data):
        return models.DeployInstance(**data)


class DeployCommentSchema(Schema):
    ID = fields.Integer(allow_none=True, attribute="id")
    creator = fields.String(allow_none=True)
    create_time = fields.DateTime(allow_none=True)
    updator = fields.String(allow_none=True)
    update_time = fields.DateTime(allow_none=True)
    content = fields.String(required=True)

    @post_load
    def make_deploy_comment(self, data):
        return models.DeployInstanceComment(**data)


class DeployFileSchema(Schema):
    ID = fields.Integer(allow_none=True, attribute="id")
    creator = fields.String(allow_none=True)
    create_time = fields.DateTime(allow_none=True)
    updator = fields.String(allow_none=True)
    update_time = fields.DateTime(allow_none=True)
    access_url = fields.String(allow_none=True)
    file_name = fields.String(allow_none=True)

    @post_load
    def make_deploy_file(self, data):
        return models.DeployInstanceFile(**data)


class ChangeSchema(Schema):
    ID = fields.Integer(allow_none=True, attribute="id")
    creator = fields.String(allow_none=True)
    create_time = fields.DateTime(allow_none=True)
    updator = fields.String(allow_none=True)
    update_time = fields.DateTime(allow_none=True)
    system = fields.String(required=True)
    change_type = fields.String(required=True)
    version = fields.String(required=True)
    db_type = fields.String(allow_none=True)
    db_config = fields.String(allow_none=True)
    db_sql = fields.String(allow_none=True)
    cc = fields.String(allow_none=True)
    dev = fields.String(allow_none=True)
    qa = fields.String(allow_none=True)
    ops = fields.String(allow_none=True)
    approver = fields.String(allow_none=True)
    dba = fields.String(allow_none=True)
    pm = fields.String(allow_none=True)
    operate_dev = fields.String(allow_none=True)
    operate_qa = fields.String(allow_none=True)
    operate_ops = fields.String(allow_none=True)
    operate_approver = fields.String(allow_none=True)
    operate_dba = fields.String(allow_none=True)
    operate_pm = fields.String(allow_none=True)
    plan_time = fields.DateTime(allow_none=True)
    problem_desc = fields.String(allow_none=True)
    content_desc = fields.String(allow_none=True)
    risk_desc = fields.String(allow_none=True)
    approver_time = fields.DateTime(allow_none=True)
    qa_time = fields.DateTime(allow_none=True)
    ops_time = fields.DateTime(allow_none=True)
    dev_time = fields.DateTime(allow_none=True)
    dba_time = fields.DateTime(allow_none=True)
    pm_time = fields.DateTime(allow_none=True)
    status = fields.Integer(allow_none=True)
    bak_status = fields.Integer(allow_none=True)

    @post_load
    def make_change(self, data):
        return models.ChangeInstance(**data)


class ChangeCommentSchema(Schema):
    ID = fields.Integer(allow_none=True, attribute="id")
    creator = fields.String(allow_none=True)
    create_time = fields.DateTime(allow_none=True)
    updator = fields.String(allow_none=True)
    update_time = fields.DateTime(allow_none=True)
    content = fields.String(required=True)

    @post_load
    def make_change_comment(self, data):
        return models.ChangeInstanceComment(**data)


class ChangeFileSchema(Schema):
    ID = fields.Integer(allow_none=True, attribute="id")
    creator = fields.String(allow_none=True)
    create_time = fields.DateTime(allow_none=True)
    updator = fields.String(allow_none=True)
    update_time = fields.DateTime(allow_none=True)
    access_url = fields.String(allow_none=True)
    file_name = fields.String(allow_none=True)

    @post_load
    def make_change_file(self, data):
        return models.ChangeInstanceFile(**data)
