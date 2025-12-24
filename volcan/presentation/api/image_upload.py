from fastapi import APIRouter, HTTPException, Request, Depends
from volcan.core.constants import images_url_prefix
from volcan.core.di.dependencies import inject_upload_use_case
from volcan.presentation.dto.image import Image
from volcan.presentation.dto.upload_response import UploadResponse

router = APIRouter()


@router.post('/upload', response_model=UploadResponse)
async def upload_image(request: Request, upload_image_use_case = Depends(inject_upload_use_case)):
    try:
        content_type = request.headers.get("content-type", "")
        if "image/png" not in content_type:
            raise HTTPException(
                status_code=400,
                detail="Only PNG files are allowed"
            )

        base_url = str(request.base_url).rstrip('/')
        filename = await upload_image_use_case.execute(stream=request.stream())
        download_url = f"{base_url}{images_url_prefix}/{filename}"
        return Image(image_url=download_url)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")