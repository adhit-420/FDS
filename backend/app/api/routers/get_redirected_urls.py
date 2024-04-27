from fastapi import APIRouter
from app.utils.get_redirected_urls import get_redirected_urls

router = APIRouter()


@router.get("/get_redirected_urls/")
async def get_redirected_urls_from_url(url: str):
    print(url)
    urls = get_redirected_urls(url)
    print(urls)
    return {"redirected_urls": urls}
