from gevent import monkey,queue
from gevent.pywsgi import WSGIServer
from flask import  Flask, render_template, request, json

app = Flask(__name__)
app.debug = True

class Room(object):
    def __init__(self):
        self.usrs = set()
        self.messages = []
    def backlog(self, size = 25):
        return self.messages[-size:]
    def subscribe(self, user):
        self.usrs.add(user)
    def add(self, message):
        for usr in self.usrs:
            usr.queue.put_nowait(message)
        self.messages.append(message)

class User(object):
    def __init__(self):
        self.queue = queue.Queue()

rooms = {
    'room1':Room(),
    'room2':Room(),
}

users = {}

@app.route('/')
def choose_name():
    return render_template('choose.html')

@app.route('/<uid>')
def main(uid):
    return render_template('main.html', uid=uid,rooms=rooms.keys())

@app.route('/<room>/<uid>')
def join(room, uid):
    user = users.get(uid, None)
    if not user:
        users[uid] = user = User()
    active_room = rooms[room]
    active_room.subscribe(user)
    messages = active_room.backlog()
    return render_template('room.html', room=room, uid=uid
                           , messages=messages)

@app.route('/put/<room>/<uid>', methods=["POST"])
def put(room, uid):
    user = users[uid]
    room = rooms[room]
    message = request.form['message']
    room.add(':'.join([uid, message]))
    return ''

@app.route("/poll/<uid>", methods=["POST"])
def poll(uid):
    try:
        msg = users[uid].queue.get(timeout=10)
    except queue.Empty:
        msg = []
    return json.dumps(msg)

http = WSGIServer(('', 5000), app)
http.serve_forever()

