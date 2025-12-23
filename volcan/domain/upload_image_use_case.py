import typing
import uuid
import injector
from volcan.constants import images_url_prefix
from volcan.domain.image import Image
from volcan.domain.image_repository import ImageRepository


class UploadImageUseCase:
    @injector.inject
    def __init__(self, repository: ImageRepository):
        self.repository = repository

    async def execute(
            self,
            base_url: str,
            stream: typing.AsyncGenerator[bytes, None],
    ) -> Image:
        file_extension = "png"
        filename = f"{uuid.uuid4()}.{file_extension}"
        await self.repository.upload_image(filename=filename, stream=stream)
        download_url = f"{base_url}{images_url_prefix}/{filename}"
        return Image(image_url=download_url)