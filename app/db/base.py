from sqlalchemy.orm import DeclarativeBase, MappedColumn, declared_attr, mapped_column
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from datetime import datetime
import uuid


class Base(DeclarativeBase):
    """Shared declarative base for all ORM models."""

    @declared_attr.directive
    @classmethod
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"
