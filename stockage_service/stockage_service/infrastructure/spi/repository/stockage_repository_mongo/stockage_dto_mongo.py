from uuid import UUID, uuid4
import traceback
from kink import di
from pydantic import Field, BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

from domains.stockage.models.prompt import Prompt


class PromptMongoDto(BaseModel):
    id: str
    content: str
    creation_date: datetime
    updated_date: datetime
    created_by: str
    tags: str
    status: str
    related_images: List[str]
    generation_origin: str = ""
    processing_duration: int = 0

    @classmethod
    def fromPrompt(cls, data: Prompt):
        return cls(
            id=str(data.id),
            content=data.content,
            creation_date=data.creation_date,
            updated_date=data.updated_date,
            created_by=data.created_by,
            tags=data.tags,
            status=data.status,
            usage_count=data.usage_count,
            related_images=data.related_images,
            generation_origin=data.generation_origin,
            processing_duration=data.processing_duration,
        )

    def toPrompt(self) -> Prompt:  # type: ignore
        try:
            instance = Prompt(
                id=str(self.id),  # type: ignore
                content=self.content,
                creation_date=self.creation_date,
                updated_date=self.updated_date,
                created_by=self.created_by,
                tags=self.tags,
                status=self.status,
                related_images=self.related_images,
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
                content=data["content"],
                creation_date=data["creation_date"],
                updated_date=data["updated_date"],
                created_by=data["created_by"],
                tags=data["tags"],
                status=data["status"],
                related_images=data["related_images"],
                generation_origin=data["generation_origin"],
                processing_duration=data["processing_duration"],
            )
            return instance
        except Exception:
            traceback.print_exc()
