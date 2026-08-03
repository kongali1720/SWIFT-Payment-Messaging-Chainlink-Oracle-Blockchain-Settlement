from fastapi import FastAPI

from api.routes import router
from api.middleware import request_timer
from api.exceptions import APIException, api_exception_handler

app = FastAPI(
    title="SWIFT Payment Messaging API",
    version="0.2.0",
    description="Enterprise SWIFT Processing Platform"
)

app.middleware("http")(request_timer)

app.add_exception_handler(APIException, api_exception_handler)

app.include_router(router)


@app.get("/")
def root():
    return {
        "name": "SWIFT Payment Messaging API",
        "version": "0.2.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
