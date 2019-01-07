# WSGI server in Python
from wsgiref.simple_server import make_server

def application (environ, start_response):
    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain')]

    start_response(status, response_headers)

    return ["welcome to gevent lesson"]

# Instantiate the WSGI server.
# It will receive the request, pass it to the application
# and send the application's response to the client
httpd = make_server(
    'localhost', # The host name.
    8080, # A port number where to wait for the request.
    application # Our application object name, in this case a function.
    )