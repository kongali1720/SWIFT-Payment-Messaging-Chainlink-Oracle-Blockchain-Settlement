from pydantic import BaseModel


class SwiftMessageRequest(BaseModel):
    message: str
