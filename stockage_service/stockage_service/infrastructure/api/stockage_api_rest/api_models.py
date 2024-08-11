from typing import Optional

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    code: int
    type: str
    message: str
