import os
import uuid
from typing import BinaryIO

from volcan.domain.image import Image
from volcan.settings import settings

class ImageUploadService:

    async def upload_image(self, file_stream: BinaryIO) -> Image:
        # Генерируем уникальное имя файла
        file_extension = "png"
        unique_filename = f"{uuid.uuid4()}.{file_extension}"

        # Полный путь к файлу
        file_path = os.path.join(settings.images_dir, unique_filename)

        # Читаем и сохраняем файл потоково
        file_size = 0
        with open(file_path, 'wb') as f:
            while True:
                # Читаем чанками по 64KB
                chunk = file_stream.read(64 * 1024)
                if not chunk:
                    break
                f.write(chunk)
                file_size += len(chunk)

        return Image(filename=unique_filename)