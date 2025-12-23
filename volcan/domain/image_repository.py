from interface import Interface, implements

from volcan.domain.image import Image
from fastapi import Request


class ImageRepository(Interface):
    async def upload_image(self, request: Request) -> Image:
        pass