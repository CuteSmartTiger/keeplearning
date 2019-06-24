# coding=utf8
import ldap
import socket
import re


class Ldap:
    """
    Ldap
    """
    HOST_PREFIX = 'ldap://'
    ERROR_MSG_1 = u"IP地址不是合法"
    ERROR_MSG_2 = u"网络连通不正常"
    ERROR_MSG_3 = u"无效的系统Credential"
    ERROR_MSG_4 = u"系统认证失败"
    ERROR_MSG_5 = u"用户名不存在"
    ERROR_MSG_6 = u"无效的Credential"
    ERROR_MSG_7 = u"认证失败"

    def __init__(self, host, port=None, dn=None, password=None, user_dn=None):
        self.host = host.replace(Ldap.HOST_PREFIX, '') if Ldap.HOST_PREFIX in host else host
        self.port = 389 if not port else port
        self.dn = dn
        self.password = password
        self.user_dn = user_dn

    @staticmethod
    def get_attr(r, attr):
        if r and (isinstance(r, list) or isinstance(r, tuple)):
            r = r[0]
        if r and (isinstance(r, list) or isinstance(r, tuple)) and len(r) >= 2:
            r = r[1]
        value = r.get(attr)
        if value and isinstance(value, list):
            value = value[0]
        return value

    def judge_legal_ip(self):
        compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        return True if compile_ip.match(self.host) else False

    def judge_connect(self):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(1)
        try:
            sk.connect((self.host, self.port))
            return True
        except Exception:
            return False
        finally:
            sk.close()

    def get_user_info(self, employee_id):
        host = '{0}{1}'.format(Ldap.HOST_PREFIX, self.host)
        l = ldap.initialize(host)
        try:
            l.protocol_version = ldap.VERSION3
            l.simple_bind_s(self.dn, self.password)
        except ldap.INVALID_CREDENTIALS:
            return False, {}, Ldap.ERROR_MSG_3
        except ldap.LDAPError:
            return False, {}, Ldap.ERROR_MSG_4
        else:
            try:
                search_filter_id = "employeeID"
                search_filter = '(' + search_filter_id + "=" + employee_id + ')'
                r = l.search_s(self.user_dn, ldap.SCOPE_SUBTREE, search_filter,
                               ['cn', 'mail', 'sAMAccountName', 'mobile'])
                cn_name = self.get_attr(r=r, attr='cn')
                email = self.get_attr(r=r, attr='mail')
                mobile = self.get_attr(r=r, attr='mobile')
                username = self.get_attr(r=r, attr='sAMAccountName')
            except Exception:
                return False, {}, Ldap.ERROR_MSG_5
            l_data = dict(cn_name=cn_name, email=email, mobile=mobile, username=username)
            return True, l_data, None
        finally:
            l.unbind_s()

    def get_user_dn(self, username):
        host = '{0}{1}'.format(Ldap.HOST_PREFIX, self.host)
        l = ldap.initialize(host)
        try:
            l.protocol_version = ldap.VERSION3
            l.simple_bind_s(self.dn, self.password)
        except ldap.INVALID_CREDENTIALS:
            return False, None, Ldap.ERROR_MSG_3
        except ldap.LDAPError:
            return False, None, Ldap.ERROR_MSG_4
        else:
            try:
                search_filter_name = "sAMAccountName"
                search_filter = '(' + search_filter_name + "=" + username + ')'
                r = l.search_s(self.user_dn, ldap.SCOPE_SUBTREE, search_filter, ['cn', 'mail'])
                user_dn = r[0][0]
            except Exception:
                return False, None, Ldap.ERROR_MSG_5
            return True, user_dn, None
        finally:
            l.unbind_s()

    def authenticate(self, username, password):
        if not self.judge_legal_ip():
            return False, {}, Ldap.ERROR_MSG_1
        if not self.judge_connect():
            return False, {}, Ldap.ERROR_MSG_2
        get_dn, user_dn, message = self.get_user_dn(username)
        if not get_dn:
            return False, {}, message
        host = '{0}{1}'.format(Ldap.HOST_PREFIX, self.host)
        l = ldap.initialize(host)
        try:
            l.protocol_version = ldap.VERSION3
            l.simple_bind_s(user_dn, password)
        except ldap.INVALID_CREDENTIALS:
            return False, {}, Ldap.ERROR_MSG_6
        except ldap.LDAPError:
            return False, {}, Ldap.ERROR_MSG_7
        else:
            try:
                r = l.search_s(user_dn, ldap.SCOPE_SUBTREE, '(objectClass=*)', ['cn', 'mail', 'mobile'])
                cn_name = self.get_attr(r=r, attr='cn')
                email = self.get_attr(r=r, attr='mail')
                mobile = self.get_attr(r=r, attr='mobile')
            except Exception:
                cn_name, email, mobile = None, None, None
            l_data = dict(cn_name=cn_name, email=email, mobile=mobile)
            return True, l_data, None
        finally:
            l.unbind_s()


if __name__ == '__main__':
    # lp = Ldap(host='10.56.10.113',
    #           dn='CN=dalmore,CN=Users,DC=corp,DC=bkjk,DC=com',
    #           password='BKJKops123!@',
    #           user_dn='OU=贝壳金控,OU=BKJK,dc=corp,dc=bkjk,dc=com')
    # check, data, msg = lp.get_user_info('20368965')
    # print(check, data, msg)
    # lp = Ldap(host='10.12.3.30',
    #           port=389,
    #           dn='CN=达尔摩,OU=贝壳,OU=理房通,DC=corp,DC=ehomepay,DC=com,DC=cn',
    #           password='LFTeh0mepay!',
    #           user_dn='OU=理房通,DC=corp,DC=ehomepay,DC=com,DC=cn')
    # check, data, msg = lp.get_user_dn('dalmore')
    # print(check, data, msg)
    pass

