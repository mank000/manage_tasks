from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from models.db import get_session
from models.models import Task
from models.schemas import TaskCreate, TaskRead, TaskUpdate
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/",
    response_model=List[TaskRead],
    status_code=status.HTTP_200_OK,
)
async def get_tasks(db: Session = Depends(get_session)):
    return db.query(Task).all()


@router.post(
    "/",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_task(task: TaskCreate, db: Session = Depends(get_session)):
    task_dict = task.model_dump()
    db_task = Task(**task_dict)

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


@router.get(
    "/{task_uuid}",
    response_model=TaskRead,
    status_code=status.HTTP_200_OK,
)
async def get_current_task(
    task_uuid: UUID, db: Session = Depends(get_session)
):
    task = db.get(Task, task_uuid)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена.")
    return task


@router.delete("/{task_uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_uuid: UUID, db: Session = Depends(get_session)):
    task = db.get(Task, task_uuid)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Запись не найдена."
        )
    db.delete(task)
    db.commit()
    return


@router.patch(
    "/{task_uuid}", status_code=status.HTTP_200_OK, response_model=TaskRead
)
async def patch_task(
    task_uuid: UUID, task_data: TaskUpdate, db: Session = Depends(get_session)
):
    task = db.get(Task, task_uuid)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Задача не найдена."
        )
    update_data = task_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


@router.put("/{task_uuid}", status_code=status.HTTP_200_OK)
async def update_task(
    task_uuid: UUID,
    task_data: TaskCreate,
    db: Session = Depends(get_session),
):
    task = db.query(Task).filter(Task.uuid == task_uuid).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена",
        )

    for field, value in task_data.model_dump().items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task
