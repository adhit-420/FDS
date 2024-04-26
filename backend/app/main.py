from fastapi import FastAPI

app = FastAPI()


# Sample endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Fraud Detection API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
