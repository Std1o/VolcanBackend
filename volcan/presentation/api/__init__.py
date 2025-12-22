from fastapi import APIRouter
from .image_upload import router as image_upload_router
from .images import router as images_router

router = APIRouter()
router.include_router(image_upload_router)
router.include_router(images_router)