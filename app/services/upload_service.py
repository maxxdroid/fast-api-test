import os
import uuid
from fastapi import UploadFile, HTTPException
from app.core.config import IMAGES_DIR, MAX_FILE_SIZE_MB, ALLOWED_EXTENSIONS

def save_image(imageFile: UploadFile) -> str:

    ext = imageFile.filename.split(".")[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    imageFile.file.seek(0, os.SEEK_END)
    size_mb = imageFile.file.tell() / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        raise HTTPException(status_code=400, detail="File too large")
    imageFile.file.seek(0)

    # Generate unique ID and save
    image_id = str(uuid.uuid4())
    file_path = os.path.join(IMAGES_DIR, f"{image_id}.{ext}")

    with open(file_path, "wb") as f:
        f.write(imageFile.file.read())

    return image_id


def get_image_path(image_id: str) -> str:
    
    # Find file in images folder
    for filename in os.listdir(IMAGES_DIR):
        if filename.startswith(image_id):
            return os.path.join(IMAGES_DIR, filename)
    raise HTTPException(status_code=404, detail="Image not found")