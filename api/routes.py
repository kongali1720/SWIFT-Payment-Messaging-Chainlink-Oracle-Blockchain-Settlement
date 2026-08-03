from fastapi import APIRouter

from api.schemas import SwiftMessageRequest
from services.swift_service import parse_mt103

router = APIRouter(
    prefix="/api/v1",
    tags=["SWIFT"],
)


@router.get("/status")
def status():
    return {
        "service": "SWIFT Engine",
        "online": True,
    }


@router.post("/swift/parse")
def parse(request: SwiftMessageRequest):
    return parse_mt103(request.message)
