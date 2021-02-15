#!/usr/bin/env python3
# based on https://pymotw.com/3/socket/tcp.html

import socket
import sys

HOST = '104.155.162.200'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = bytes('ping to server ' + socket.gethostname() + ':' + str(PORT), 'utf-8')
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    #amount_received = 0
    #amount_expected = len(message)
    #amount_expected = 64

    #while amount_received < amount_expected:
    #    data = sock.recv(16)
    #    amount_received += len(data)
    #    print('received {!r}'.format(data))
    data = sock.recv(1024)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
