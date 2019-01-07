import SocketServer
import time
port = 5000
class MyRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data or len(data) == 0:
                return
            print data
        return

address = ('localhost', port)
server = SocketServer.TCPServer(address, MyRequestHandler)
server.serve_forever()