import pytest
from fastapi.testclient import TestClient
from main import app
from models.db import get_session
from sqlmodel import Session, SQLModel, create_engine

SQLALCHEMY_DATABASE_URL = "sqlite:///task_test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


@pytest.fixture(name="session")
def session_fixture():
    """Создаёт таблицы перед тестами и очищает после."""
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(name="client")
def client_fixture(session: Session):
    """Подменяем get_session на фикстурную сессию."""

    def override_get_session():
        yield session

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as c:
        yield c
