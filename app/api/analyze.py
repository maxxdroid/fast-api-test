from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.deps import get_api_key
from app.services.analyze_service import analyze_image
from app.services.upload_service import get_image_path


router = APIRouter(dependencies=[Depends(get_api_key)] )

class AnalyzeRequest(BaseModel):
    image_id: str


@router.post("/analyze")
def analyze_image_endpoint(request: AnalyzeRequest):
    # Check if image exists
    get_image_path(request.image_id)
    # Run  analysis
    result = analyze_image(request.image_id)
    return result