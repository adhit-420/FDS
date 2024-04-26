from fastapi import APIRouter
from app.utils.get_redirected_urls import get_redirected_urls

router = APIRouter()

@router.get("/get_redirected_urls/{url}")
async def get_redirected_urls_from_url(url: str):
    return get_redirected_urls(url)

