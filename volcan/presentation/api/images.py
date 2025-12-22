from fastapi import APIRouter
from fastapi.responses import FileResponse

from volcan.settings import settings

router = APIRouter(prefix=settings.images_url_prefix)

@router.get('/{image_name}')
def get_image(image_name: str):
    return FileResponse(f"{settings.images_dir}/{image_name}")