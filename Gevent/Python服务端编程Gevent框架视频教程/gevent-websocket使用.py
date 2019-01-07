from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi, sleep
import random
import json
```PYTHON


class WebSocketApp(object):
    def __call__(self, env, start_response):
        ws = env['wsgi.websocket']
        x = 0
        while True:
            data = json.dumps({'x': x, 'y': random.randint(1, 5)})
            ws.send(data)
            x += 1
            sleep(0.5)


server = pywsgi.WSGIServer(('', 8800), WebSocketApp(),
                           handler_class=WebSocketHandler)
server.serve_forever()


```
