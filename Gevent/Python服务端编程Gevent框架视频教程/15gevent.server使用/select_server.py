import socket, select
port = 5000

if __name__ == "__main__":
    read_list = []    # list of socket clients
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    client_map = {}
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((“localhost", port))
    server_socket.listen(10)
    # Add server socket to the list of readable connections
    read_list.append(server_socket)
    while Ture:
        read_sockets,write_sockets,error_sockets = select.select(read_list, [], [])
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                print "Client (%s, %s) connected" % addr
                read_list.append(sockfd)
                client_map[sockfd] = addr
            #Some incoming message from a client
            else:
                data = sock.recv(1024)
                if len(data) == 0:
                    if sock in client_map:
                        print "client (%s,%s) closed", client_map[sock]
                    del client_map[sock]
                     read_list.remove(sock)
                else:
                    print "get ", data

    server_socket.close()