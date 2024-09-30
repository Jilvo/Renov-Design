import traceback
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

from stockage_service.domains.stockage.models.prompt import Prompt


class PromptMongoDto(BaseModel):
    id: str
    creation_date: datetime
    updated_date: datetime
    created_by: str
    tags: str
    status: str
    modified_image: List[str]
    generation_origin: str = ""
    processing_duration: int = 0

    @classmethod
    def fromPrompt(cls, data: Prompt):
        return cls(
            id=str(data.id),
            creation_date=data.creation_date,
            updated_date=datetime.now(),
            created_by=data.created_by,
            tags=data.tags,
            status=data.status,
            modified_image=data.modified_image,
            generation_origin=data.generation_origin,
            processing_duration=data.processing_duration,
        )

    def toPrompt(self) -> Prompt:  # type: ignore
        try:
            instance = Prompt(
                id=str(self.id),  # type: ignore
                creation_date=self.creation_date,
                updated_date=self.updated_date,
                created_by=self.created_by,
                tags=self.tags,
                status=self.status,
                modified_image=self.modified_image,
                generation_origin=self.generation_origin,
                processing_duration=self.processing_duration,
            )

            return instance
        except Exception:
            traceback.print_exc()

    @classmethod
    def fromDict(cls, data: Dict):
        try:
            instance = cls(
                id=data["id"],
                creation_date=data["creation_date"],
                updated_date=data["updated_date"],
                created_by=data["created_by"],
                tags=data["tags"],
                status=data["status"],
                modified_image=data["modified_image"],
                generation_origin=data["generation_origin"],
                processing_duration=data["processing_duration"],
            )
            return instance
        except Exception:
            traceback.print_exc()
