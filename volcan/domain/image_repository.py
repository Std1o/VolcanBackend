import typing
from interface import Interface, implements
from volcan.domain.image import Image


class ImageRepository(Interface):
    async def upload_image(self, stream: typing.AsyncGenerator[bytes, None]) -> Image:
        pass