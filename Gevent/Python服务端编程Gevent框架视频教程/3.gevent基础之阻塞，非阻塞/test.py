import logging
import time
import errno

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',)

if __name__ == '__main__':
    import socket

    ip = 'localhost'
    port = 58562

    logger = logging.getLogger('client')

    # Connect to the server
    logger.debug('creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug('connecting to server')

    s.setblocking(0)
    try:
        s.connect((ip, port))
    except socket.error, msg:
        if msg[0] != errno.EINPROGRESS:
            logger.debug('error')
            exit(1)

    #time.sleep(1)

    # Send the data
    message = 'Hello, world'
    #len_sent = s.send(message)
    logger.debug('sending data: "%s"', message)
    while True:
        try:
            len_sent = s.send(message)
            break
        except socket.error, msg:
            if msg[0] != errno.EAGAIN:
                exit(1)

    # Receive a response
    logger.debug('waiting for response')
    while True:
        try:
            response = s.recv(len_sent)
            break
        except socket.error, msg:
            if msg[0] != errno.EAGAIN:
                exit(1)
    logger.debug('response from server: "%s"', response)

    # Clean up
    logger.debug('closing socket')
    s.close()
    logger.debug('done')