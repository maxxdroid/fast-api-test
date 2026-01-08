from fastapi import APIRouter

router = APIRouter()

@router.get("/upload")
def get_upload():
    return "Hola Mf"