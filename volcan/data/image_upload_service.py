import os
import typing
import aiofiles
from volcan.domain.image import Image
from volcan.settings import settings


class ImageUploadService:

    async def upload_image(self, filename: str, stream: typing.AsyncGenerator[bytes, None]) -> Image:
        file_path = os.path.join(settings.images_dir, filename)

        # Читаем и сохраняем файл потоково
        async with aiofiles.open(file_path, 'wb') as f:
            async for chunk in stream:
                await f.write(chunk)

        return Image(filename=filename)
