from fastapi import APIRouter, File, UploadFile
from app.services.upload_service import save_image

router = APIRouter()

@router.get("/upload")
def get_upload():
    return "Hola Mf"

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    """
    Upload an image (JPEG/PNG, max 5MB)
    """
    image_id = save_image(file)
    return {"image_id": image_id}