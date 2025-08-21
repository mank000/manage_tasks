from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel

from .enums import TaskStatus


class Task(SQLModel, table=True):
    """Модель задачи для бд."""

    uuid: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        description="Уникальный номер задачи",
    )
    name: str = Field(
        max_length=100,
        index=True,
        nullable=False,
        description="Название задачи",
    )

    description: Optional[str] = Field(
        default=None,
        max_length=512,
        nullable=True,
        description="Описание задачи",
    )

    status: TaskStatus = Field(
        default=TaskStatus.CREATED,
        nullable=False,
        description="Статус задачи",
    )
