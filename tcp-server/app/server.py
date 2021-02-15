#!/usr/bin/env python3
# based on https://pymotw.com/3/socket/tcp.html

import socket
import sys

PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', PORT)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        #while True:
        data = connection.recv(1024)
        print('received {!r}'.format(data))
        if data:
            print('sending response back to the client')
            response = 'pong from ' + socket.gethostname()
            connection.sendall(bytes(response, 'utf-8'))
        else:
            print('no data from', client_address)
            break

    finally:
        # Clean up the connection
        connection.close()