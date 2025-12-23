import typing
from interface import implements
from volcan.data.image_upload_service import ImageUploadService
from volcan.domain.image import Image
from volcan.domain.image_repository import ImageRepository
from fastapi import Request


class ImageRepositoryImpl(implements(ImageRepository)):
    async def upload_image(self, stream: typing.AsyncGenerator[bytes, None]) -> Image:
        service = ImageUploadService()
        return await service.upload_image(stream)