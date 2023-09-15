import asyncio
from time import sleep
import datetime
import logging

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        host='34.118.239.118', port=8888)

    logging.info(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    logging.info(f'Received: {data.decode()!r}')

    logging.info('Close the connection')
    writer.close()
    await writer.wait_closed()

# run forever
while True:

    try: 
        asyncio.run(tcp_echo_client(f'Hello World at {datetime.datetime.now()}!'))
        sleep(1)
    except:
        logging.error("Unable to connect to server")
        sleep(1)