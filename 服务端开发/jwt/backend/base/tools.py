# coding = utf8
import sys
import socket
import codecs
import datetime
import platform

if sys.stdout.encoding.upper() != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding.upper() != 'UTF-8':
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


def utc_now():
    return datetime.datetime.utcnow()


def now():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=8)


def str2datetime(date_str, _format='%Y-%m-%d %H:%M', _utc=False):
    date = datetime.datetime.strptime(date_str, _format)
    if _utc:
        return date - datetime.timedelta(hours=8)
    else:
        return date


def check_ip_port(ip, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((ip, port))
        return True
    except Exception:
        return False
    finally:
        sk.close()


def is_linux_system():
    return 'Linux' in platform.system()

