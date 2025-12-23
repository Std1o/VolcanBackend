from fastapi import APIRouter
from fastapi.responses import FileResponse
from volcan.core.constants import images_url_prefix, images_dir

router = APIRouter(prefix=images_url_prefix)

@router.get('/{image_name}')
def get_image(image_name: str):
    return FileResponse(f"{images_dir}/{image_name}")