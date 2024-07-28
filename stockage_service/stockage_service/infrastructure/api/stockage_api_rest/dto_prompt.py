from pydantic import BaseModel
from typing import List, Optional


class PromptRequest(BaseModel):
    content: str
    created_by: str
    tags: Optional[str]
    status: str
    related_images: Optional[List[str]]
    generation_origin: Optional[str]
    processing_duration: Optional[int]


class PromptResponse(BaseModel):
    code: int
    type: str
    message: str

    class Config:
        # TODO corriger example
        schema_extra = {
            "example": {
                "code": "200",
                "type": "",
                "message": "",
            },
        }
