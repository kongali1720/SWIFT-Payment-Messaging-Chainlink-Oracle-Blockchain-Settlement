from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="SWIFT Payment Messaging API",
    version="0.1.0",
    description="Enterprise Settlement Infrastructure"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "project": "SWIFT Payment Messaging",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
