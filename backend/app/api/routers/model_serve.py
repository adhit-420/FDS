from fastapi import APIRouter, Depends
from app.api.models.phish_model import RFModel

router = APIRouter()


@router.get("/phish_model")
async def predict_phish_model(url: str):
    return RFModel().predict([url])[0]
