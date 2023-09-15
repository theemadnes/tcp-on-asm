import asyncio
import logging

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    logging.info(f"Received {message!r} from {addr!r}")

    logging.info(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    logging.info("Close the connection")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_echo, '0.0.0.0', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    logging.info(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())