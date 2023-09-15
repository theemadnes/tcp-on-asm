import socket
import os
import datetime
from time import sleep

HOST = os.environ.get(key="HOST", default="tcp-server")
PORT = os.environ.get(key="PORT", default=8888)

while True: 

    try:
        data = f"hi at {datetime.datetime.now()}"

        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data + "\n", "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

        print("Sent:     {}".format(data))
        print("Received: {}".format(received))

    except:
        print("Error")

    sleep(1)
