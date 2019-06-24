# coding=utf8
import jwt
import datetime
from config import config


class JWT:
    """
    JWT
    """
    EXP = 30
    ISS = 'blaze.hu'

    @staticmethod
    def encode_auth_token(username, last_login):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=JWT.EXP),
                'iat': datetime.datetime.utcnow(),
                'iss': JWT.ISS,
                'data': {
                    'username': username,
                    'last_login': last_login.strftime('%Y-%m-%d %H:%M')
                }
            }
            return jwt.encode(
                payload,
                config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            # 过期时间验证
            payload = jwt.decode(auth_token, config.SECRET_KEY, leeway=datetime.timedelta(days=JWT.EXP))
            if 'data' in payload and 'username' in payload['data']:
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return 'Token无效'

    def identify(self, request):
        auth_header = request.headers.get(config.TOKEN_HEADER_KEY)
        is_identified = False
        username = None
        if auth_header:
            auth_token_list = auth_header.split(" ")
            if not auth_token_list or auth_token_list[0] != config.TOKEN_HEADER_VALUE_FLAG or len(auth_token_list) != 2:
                msg = "验证失败，请传递正确的验证头信息"
            else:
                auth_token = auth_token_list[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    data = payload.get('data')
                    username = data.get('username')
                    is_identified = True
                    msg = "验证通过"
                else:
                    msg = "验证Token失败，{detail_msg}".format(detail_msg=payload)
        else:
            msg = "请先登录..."  # 没有Token
        return is_identified, msg, username


if __name__ == '__main__':
    pass
