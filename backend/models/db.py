from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine

from .models import Task

DATABASE_URL = "sqlite:///./db.sqlite3"


engine: Engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    """Создает все таблицы в базе данных."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Генератор сессий для зависимостей."""
    with Session(engine) as session:
        yield session
