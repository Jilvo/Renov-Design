from pydantic import BaseModel
from typing import Optional


class PromptRequest(BaseModel):
    created_by: str
    tags: Optional[str]
    status: str
    modified_image: Optional[str]
    generation_origin: str
    processing_duration: Optional[float]


class PromptResponse(BaseModel):
    code: int
    type: str
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "code": 200,
                "type": "success",
                "message": "Prompt created successfully",
            },
        }
