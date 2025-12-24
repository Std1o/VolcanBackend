import typing
from interface import implements
from volcan.data.image_upload_service import ImageUploadService
from volcan.domain.image_repository import ImageRepository


class ImageRepositoryImpl(implements(ImageRepository)):
    async def upload_image(self, filename: str, stream: typing.AsyncGenerator[bytes, None]):
        service = ImageUploadService()
        return await service.upload_image(filename=filename,stream=stream)