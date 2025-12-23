import injector
from fastapi import APIRouter, HTTPException, Request
from volcan.core.di import ImageModule
from volcan.domain.upload_image_use_case import UploadImageUseCase
from volcan.presentation.dto.upload_response import UploadResponse

router = APIRouter()


@router.post('/upload', response_model=UploadResponse)
async def upload_image(request: Request):
    try:
        content_type = request.headers.get("content-type", "")
        if "image/png" not in content_type:
            raise HTTPException(
                status_code=400,
                detail="Only PNG files are allowed"
            )

        injector_instance = injector.Injector([ImageModule()])

        upload_image_use_case = injector_instance.get(UploadImageUseCase)
        base_url = str(request.base_url).rstrip('/')
        image = await upload_image_use_case.execute(base_url=base_url, stream=request.stream())
        return image

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")