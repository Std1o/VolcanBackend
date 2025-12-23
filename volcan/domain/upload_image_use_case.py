import typing
import uuid
import injector
from volcan.domain.image_repository import ImageRepository


class UploadImageUseCase:
    @injector.inject
    def __init__(self, repository: ImageRepository):
        self.repository = repository

    async def execute(
            self,
            stream: typing.AsyncGenerator[bytes, None],
    ) -> str:
        file_extension = "png"
        filename = f"{uuid.uuid4()}.{file_extension}"
        await self.repository.upload_image(filename=filename, stream=stream)
        return filename