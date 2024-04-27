from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.routers.get_redirected_urls import router as redirected_urls_router
from app.api.routers.model_serve import router as model_serve_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(redirected_urls_router)
app.include_router(model_serve_router)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Fraud Detection API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
