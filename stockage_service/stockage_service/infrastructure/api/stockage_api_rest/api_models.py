from typing import Optional

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status_code: int
    details: Optional[str]
