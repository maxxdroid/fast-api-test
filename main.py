from fastapi import FastAPI, Depends
from app.api import upload, analyze
from app.api.deps import get_api_key

app = FastAPI(
    title="Image Analysis API",
    description="Upload images and get mock AI analysis",
    version="1.0.0",
    dependencies=[Depends(get_api_key)] 
)

##Including Routers
app.include_router(upload.router)
app.include_router(analyze.router)