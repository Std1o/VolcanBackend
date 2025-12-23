# клиент для теста upload изображения

import asyncio
import aiohttp
from volcan.core.constants import CHUNK_SIZE


async def stream_upload(file_path, url):
    async with aiohttp.ClientSession() as session:
        with open(file_path, 'rb') as f:
            async def file_stream():
                while True:
                    chunk = f.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    yield chunk

            async with session.post(
                    url,
                    data=file_stream(),
                    headers={'Content-Type': 'image/png'}
            ) as response:
                return await response.json()


async def main():
    print(await stream_upload('SMA.png', 'http://192.168.1.12:80/upload'))

asyncio.run(main())