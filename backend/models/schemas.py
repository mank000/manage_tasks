from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from .enums import TaskStatus


class TaskCreate(BaseModel):
    name: str
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.CREATED

    class Config:
        from_attributes = True
        use_enum_values = True


class TaskRead(BaseModel):
    uuid: UUID
    name: str
    description: Optional[str]
    status: TaskStatus

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
