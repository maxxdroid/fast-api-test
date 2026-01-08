from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from app.services.upload_service import save_image
import os
from app.services.upload_service import get_image_path

router = APIRouter()


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    """
    Upload an image (JPEG/PNG, max 5MB)
    """
    image_id = save_image(file)
    return {"image_id": image_id}


@router.get("/images/{image_id}")
def serve_image(image_id: str):
    """
    Return the uploaded image so it can be viewed in browser
    """
    file_path = get_image_path(image_id)  # Find the file
    return FileResponse(path=file_path, media_type="image/jpeg", filename=os.path.basename(file_path))