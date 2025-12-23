import typing

import injector

from volcan.domain.image import Image
from volcan.domain.image_repository import ImageRepository


class UploadImageUseCase:
    @injector.inject
    def __init__(self, repository: ImageRepository):
        self.repository = repository

    async def execute(
            self,
            stream: typing.AsyncGenerator[bytes, None],
    ) -> Image:
        return await self.repository.upload_image(stream)