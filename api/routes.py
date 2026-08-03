from fastapi import APIRouter

from api.schemas import SwiftMessageRequest
from services.swift_service import parse

router = APIRouter(
    prefix="/api/v1",
    tags=["SWIFT"],
)


@router.get("/status")
def status():

    return {
        "status": "running"
    }


@router.post("/swift/parse")
def parse_swift(request: SwiftMessageRequest):

    return parse(request.message)
