import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class TimestampSchema(BaseSchema):
    created_at: datetime
    updated_at: datetime


class UUIDSchema(BaseSchema):
    id: uuid.UUID


class PaginatedResponse[T](BaseSchema):
    items: list[T]
    total: int
    page: int
    page_size: int
    pages: int


class HealthResponse(BaseSchema):
    status: str
    version: str
    environment: str
