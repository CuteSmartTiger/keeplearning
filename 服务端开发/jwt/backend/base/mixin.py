# encoding=utf-8
import datetime
from functools import wraps

from sanic.response import json

import const
from core import models
from base import light_jwt, light_ldap


def login_required(func):
    @wraps(func)
    async def decorated_function(self, request, *args, **kwargs):
        # run some method that checks the request
        # for the client's authorization status
        auth = light_jwt.JWT()
        is_authorized, msg, username = auth.identify(request)
        if is_authorized:
            # the user is authorized.
            # run the handler method and return the response
            request['username'] = username
            response = await func(self, request, *args, **kwargs)
            return response
        else:
            # the user is not authorized.
            return json({"code": const.FAIL_STATUS, "msg": msg})

    return decorated_function


class Auth:
    """
    JWT
    """

    @staticmethod
    def authenticate(tenant_name, username, password):
        try:
            tenant = models.Tenant.get(models.Tenant.name == tenant_name)
        except models.Tenant.DoesNotExist:
            return False, None, u"获取Tenant失败"
        # check ldap
        lp = light_ldap.Ldap(host=tenant.ad_server_uri,
                             dn=tenant.admin_ad,
                             password=tenant.admin_password,
                             user_dn=tenant.ad_bind_dn)
        is_authorized, data, msg = lp.authenticate(username, password)
        if is_authorized:
            # get or create user info
            utc_now = datetime.datetime.utcnow()
            try:
                user = models.User.get(models.User.username == username)
            except models.User.DoesNotExist:
                user = models.User()
                user.username = username
                user.date_joined = utc_now
            user.tenant = tenant
            if data.get('cn_name'):
                user.name = data.get('cn_name')
            if data.get('email'):
                user.email = data.get('email')
            if data.get('mobile'):
                user.phone = data.get('mobile')
            user.last_login = utc_now
            user.save()
            # given the default role
            src_user_roles = user.user_user_roles
            src_roles = [user_role.role.code for user_role in src_user_roles]
            if not src_roles:
                default_role = models.Role.get(models.Role.code == const.DEV)
                user_role = models.UserRole()
                user_role.user = user
                user_role.role = default_role
                user_role.save()
            # generate token
            auth = light_jwt.JWT()
            token = auth.encode_auth_token(username, utc_now)
        else:
            return False, None, msg
        return is_authorized, token, msg


class PaginateMixin(object):
    """
    object paginate
    """
    range = 5

    def paginate(self, objects, page, page_size):
        # 总的行数
        page = int(page)
        page_size = int(page_size)
        total_records = objects.count()
        # 每页大小
        page_size = page_size if page_size > 0 else 1
        # 总的页数
        total_page = int(total_records / page_size) + 1 if total_records % page_size else int(total_records / page_size)
        # 页码
        page = page if page > 0 else 1
        page = page if page < total_page else total_page
        # 是否有页 头和尾
        page_header, page_footer = 1, total_page
        has_page_header, has_page_footer = True, True
        if self.range >= total_page:
            page_range = range(1, total_page + 1)
            has_page_header = False
            has_page_footer = False
        elif page < self.range:
            page_range = range(1, self.range + 1)
            has_page_header = False
        elif page + self.range > total_page + 1:
            page_range = range(total_page + 1 - self.range, total_page + 1)
            has_page_footer = False
        else:
            page_range = range(page - 2, page + 3)

        partial = objects.paginate(page, page_size)
        paginator = dict(page=page,
                         page_size=page_size,
                         page_range=[i for i in page_range],
                         has_page_header=has_page_header,
                         has_page_footer=has_page_footer,
                         page_header=page_header,
                         page_footer=page_footer,
                         total=total_records,
                         total_page=total_page,
                         has_previous=page > 1,
                         has_next=page < total_page,
                         previous_page_number=page - 1 if page > 1 else 1,
                         next_page_number=page + 1 if page < total_page else total_page)

        return partial, paginator
