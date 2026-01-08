from fastapi import FastAPI, HTTPException
from app.api import upload, analyze

app = FastAPI(
    title="Image Analysis API",
    description="Upload images and get mock AI analysis",
    version="1.0.0"
)

##Including Routers
app.include_router(upload.router)
app.include_router(analyze.router)