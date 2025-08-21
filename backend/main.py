from typing import Union

from fastapi import FastAPI
from models.db import create_db_and_tables, get_session
from routers import tasks

app = FastAPI(
    title="task manager",
)

create_db_and_tables()

app.include_router(tasks.router)
