from gevent.pywsgi import WSGIServer
from gevent.event import Event
from cgi import escape
import uuid
import urlparse
import string
import random

def get_request_data(field, env):
    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    request_body = env['wsgi.input'].read(request_body_size)
    d = urlparse.parse_qs(request_body)
    data = d.get(field, [''])[0]
    return data

def generate_response_data(response_body, start_response):
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
    start_response('200 OK', response_headers)
    return [response_body]

def generate_json_data(msg_list):
    msg_dict = {}
    msg_dict["html"] = ""
    for msg in msg_list:
        msg_dict["html"] += "<div>{0}</div>".format(msg["msg"])
    msg_dict["id"] = msg_list[-1]["id"]
    res =  str(msg_dict)
    return res

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

file = open('longpooling.html')
chat_html = file.read()

class MessgaeBuffer(object):
    def __init__(self):
        self.cache = []
        self.message_event = Event()
    def empty(self):
        return len(self.cache) == 0

def application(env, start_response):
    env_val = env['PATH_INFO']
    if env_val == "/create":
        msg_item = {}
        msg_item["id"] = str(uuid.uuid4())
        msg_item["msg"] = id_generator()
        print "create msg %s" % str(msg_item)

        msgBuffer.cache.append(msg_item)
        msgBuffer.message_event.set()
        msgBuffer.message_event.clear()

        return generate_response_data("", start_response)
    elif env_val == "/update":
        lastid = escape(get_request_data("id", env))
        if msgBuffer.empty() or msgBuffer.cache[-1]["id"] == lastid:
            msgBuffer.message_event.wait()
        for index,m in enumerate(msgBuffer.cache):
            if m["id"] == lastid:
                return generate_response_data(generate_json_data(msgBuffer.cache[index+1:])
                                              , start_response)
        return generate_response_data(generate_json_data(msgBuffer.cache), start_response)
    else:
        return generate_response_data(chat_html, start_response)

msgBuffer = MessgaeBuffer()

WSGIServer(('localhost', 8080), application).serve_forever()
