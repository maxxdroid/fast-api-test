from fastapi import APIRouter
from pydantic import BaseModel
from app.services.analyze_service import analyze_image
from app.services.upload_service import get_image_path


router = APIRouter()

class AnalyzeRequest(BaseModel):
    image_id: str


@router.post("/analyze")
def analyze_image_endpoint(request: AnalyzeRequest):
    # Check if image exists
    get_image_path(request.image_id)
    # Run  analysis
    result = analyze_image(request.image_id)
    return result