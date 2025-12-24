import typing
from interface import Interface


class ImageRepository(Interface):
    async def upload_image(self, filename: str, stream: typing.AsyncGenerator[bytes, None]):
        pass