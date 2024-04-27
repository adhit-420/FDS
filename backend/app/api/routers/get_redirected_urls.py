from fastapi import APIRouter
from app.utils.get_redirected_urls import get_redirected_urls
import requests
router = APIRouter()


@router.get("/get_redirected_urls/")
async def get_redirected_urls_from_url(url: str):
    print(url)
    urls = get_redirected_urls(url)
    print(urls)
    return {"redirected_urls": urls}

@router.get("/get_malicious_urls")
async def get_malicious_urls(url: str):
    urls = get_redirected_urls(url)
    flagged_urls = []
    for url in urls:
        response = requests.get(f"http://localhost:8000/phish_model?url={url[1]}")
        data = response.json()
        if data["proba"] > 0.75:
            flagged_urls.append(url)
    return {"malicious_urls": flagged_urls}

