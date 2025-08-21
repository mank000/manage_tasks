from models.enums import TaskStatus


def test_create_task(client):
    response = client.post(
        "/tasks/",
        json={
            "name": "Test Task",
            "description": "Testing",
            "status": "Создано",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Task"
    assert data["description"] == "Testing"
    assert data["status"] == TaskStatus.CREATED.value
    assert "uuid" in data


def test_get_tasks(client):
    client.post(
        "/tasks/",
        json={"name": "Task1", "description": "Desc1", "status": "Создано"},
    )
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_current_task(client):
    response_create = client.post(
        "/tasks/",
        json={"name": "Task2", "description": "Desc2", "status": "Создано"},
    )
    task_uuid = response_create.json()["uuid"]

    response = client.get(f"/tasks/{task_uuid}")
    assert response.status_code == 200
    data = response.json()
    assert data["uuid"] == task_uuid


def test_patch_task(client):
    response_create = client.post(
        "/tasks/",
        json={"name": "Task3", "description": "Desc3", "status": "Создано"},
    )
    task_uuid = response_create.json()["uuid"]

    response = client.patch(
        f"/tasks/{task_uuid}",
        json={"name": "Updated Task3", "status": "В работе"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Task3"
    assert data["status"] == TaskStatus.IN_WORKING.value


def test_put_task(client):
    response_create = client.post(
        "/tasks/",
        json={"name": "Task4", "description": "Desc4", "status": "Создано"},
    )
    task_uuid = response_create.json()["uuid"]

    response = client.put(
        f"/tasks/{task_uuid}",
        json={
            "name": "Replaced Task4",
            "description": "New Desc4",
            "status": "Завершено",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Replaced Task4"
    assert data["description"] == "New Desc4"
    assert data["status"] == TaskStatus.FINISHED.value


def test_delete_task(client):
    response_create = client.post(
        "/tasks/",
        json={"name": "Task5", "description": "Desc5", "status": "Создано"},
    )
    task_uuid = response_create.json()["uuid"]

    response = client.delete(f"/tasks/{task_uuid}")
    assert response.status_code == 204

    # Проверяем, что задачи больше нет
    response_get = client.get(f"/tasks/{task_uuid}")
    assert response_get.status_code == 404
