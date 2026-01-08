from fastapi import APIRouter

router = APIRouter()

@router.get("/analyze")
def get_upload():
    return "Hola Mf"