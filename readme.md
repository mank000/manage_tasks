# Tasks Manager

## Установка и запуск

### 1. Сборка и запуск через Docker Compose

```bash
docker-compose up --build
```

## Основные эндпоинты

GET http://localhost:8000/tasks/ Получить список задач

POST http://localhost:8000/tasks/ Создать новую задачу

GET http://localhost:8000/tasks/{uuid} Получить задачу по UUID

PATCH http://localhost:8000/tasks/{uuid} Частично обновить задачу

PUT http://localhost:8000/tasks/{uuid} Полностью обновить задачу

DELETE http://localhost:8000/tasks/{uuid} Удалить задачу

## Автоматические тесты

```bash
cd backend/

pytest
```

## Документация

http://localhost:8000/docs/

http://localhost:8000/redoc/
