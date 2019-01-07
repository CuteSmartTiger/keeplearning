from flask import  Flask
import gevent.pywsgi
import gevent

app = Flask(__name__)

@app.route('/')
def handle():
    return 'welcome to gevent lesson!'

gevent_server = gevent.pywsgi.WSGIServer(('', 5000), app)
gevent_server.serve_forever()