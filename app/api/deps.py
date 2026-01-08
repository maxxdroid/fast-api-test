from fastapi import Header, HTTPException
from app.core.config import API_KEY

def get_api_key(x_api_key: str = Header(...)):
    """
    Dependency to verify API key from header: X-API-KEY
    """
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key")
    return x_api_key
