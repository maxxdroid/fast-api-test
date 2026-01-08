from fastapi import FastAPI, Depends, Request
import logging

from fastapi.responses import RedirectResponse
from app.api import upload, analyze
from app.api.deps import get_api_key


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("max_logger") 

app = FastAPI(
    title="Image Analysis API",
    description="Upload images and get mock AI analysis",
    version="1.0.0",
    # dependencies=[Depends(get_api_key)] 
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Log the incoming request
    logger.info(f"Incoming request: {request.method} {request.url}")

    # Process the request
    response = await call_next(request)

    # Log the response status code
    logger.info(f"Response status: {response.status_code} for {request.method} {request.url}")
    
    return response


@app.get("/", include_in_schema=False, dependencies=[])
def root():
    """
    Root endpoint. Redirects to Swagger UI.
    """
    return RedirectResponse(url="/docs")

##Including Routers
app.include_router(upload.router)
app.include_router(analyze.router)