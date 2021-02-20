#!/usr/bin/env python3
# based on https://asyncio.readthedocs.io/en/latest/tcp_echo.html

import socket
import asyncio

PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))

    response = 'pong from ' + socket.gethostname()

    print("Send: %r" % response)
    writer.write(bytes(response, 'utf-8'))
    await writer.drain()

    print("Close the client socket")
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', PORT, loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
