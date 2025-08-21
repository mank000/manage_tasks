from enum import Enum


class TaskStatus(str, Enum):
    """Enum для статуса."""

    CREATED = "Создано"
    IN_WORKING = "В работе"
    FINISHED = "Завершено"
