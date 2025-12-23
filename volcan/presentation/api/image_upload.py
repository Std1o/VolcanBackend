import injector
from fastapi import APIRouter, HTTPException, Depends, Request

from volcan.core.di import ImageModule
from volcan.data.image_upload_service import ImageUploadService
from volcan.domain.image_repository import ImageRepository
from volcan.presentation.dto.upload_response import UploadResponse
from volcan.settings import settings

router = APIRouter()


@router.post('/upload', response_model=UploadResponse)
async def upload_image(
        request: Request,
        service: ImageUploadService=Depends()
):
    try:
        content_type = request.headers.get("content-type", "")
        if "image/png" not in content_type:
            raise HTTPException(
                status_code=400,
                detail="Only PNG files are allowed"
            )

        injector_instance = injector.Injector([ImageModule()])

        image_repository = injector_instance.get(ImageRepository)
        image = await image_repository.upload_image(request=request)

        base_url = str(request.base_url).rstrip('/')
        download_url = f"{base_url}{settings.images_url_prefix}/{image.filename}"

        return UploadResponse(image_url=download_url)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")