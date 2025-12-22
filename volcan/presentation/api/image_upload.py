from fastapi import APIRouter, HTTPException, File, UploadFile, Depends, Request

from volcan.data.image_upload_service import ImageUploadService
from volcan.presentation.dto.upload_response import UploadResponse
from volcan.settings import settings

router = APIRouter()


@router.post('/upload', response_model=UploadResponse)
async def upload_image(
        request: Request,
        file: UploadFile,
        service: ImageUploadService=Depends()
):
    try:
        if file.content_type != "image/png":
            raise HTTPException(
                status_code=400,
                detail="Only PNG files are allowed"
            )
        image = await service.upload_image(file.file)

        base_url = str(request.base_url).rstrip('/')
        download_url = f"{base_url}{settings.images_url_prefix}/{image.filename}"

        return UploadResponse(image_url=download_url)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")