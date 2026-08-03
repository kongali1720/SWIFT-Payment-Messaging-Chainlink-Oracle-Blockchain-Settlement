from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1",
    tags=["SWIFT"]
)


@router.get("/status")
def status():
    return {
        "service": "SWIFT Engine",
        "online": True
    }
