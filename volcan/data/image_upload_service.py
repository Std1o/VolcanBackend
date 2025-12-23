import os
import typing
import uuid
import aiofiles
from volcan.domain.image import Image
from volcan.settings import settings

class ImageUploadService:

    async def upload_image(self, stream: typing.AsyncGenerator[bytes, None]) -> Image:
        # Генерируем уникальное имя файла
        file_extension = "png"
        unique_filename = f"{uuid.uuid4()}.{file_extension}"

        # Полный путь к файлу
        file_path = os.path.join(settings.images_dir, unique_filename)

        # Читаем и сохраняем файл потоково
        async with aiofiles.open(file_path, 'wb') as f:
            async for chunk in stream:
                await f.write(chunk)

        return Image(filename=unique_filename)