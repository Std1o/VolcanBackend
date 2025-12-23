import os
import typing
import aiofiles
from volcan.core.constants import images_dir


class ImageUploadService:

    async def upload_image(self, filename: str, stream: typing.AsyncGenerator[bytes, None]):
        file_path = os.path.join(images_dir, filename)

        # Читаем и сохраняем файл потоково
        async with aiofiles.open(file_path, 'wb') as f:
            async for chunk in stream:
                await f.write(chunk)
