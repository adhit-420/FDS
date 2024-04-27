from fastapi import APIRouter, Depends
from app.api.models.phish_model import RFModel
from pydantic import BaseModel


router = APIRouter()


# Define the input data model
class InputData(BaseModel):
    url: str


# Define the output data model
class OutputData(BaseModel):
    prediction: int
    probabilities: int


@router.get("/phish_model")
async def predict_phish_model(url: str):
    model = RFModel()
    pred = model.predict([url])[0]
    proba = max(model.predict_proba([url])[0])
    print(pred)
    print(proba)
    return {"pred": pred, "proba": proba}
