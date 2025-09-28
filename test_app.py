import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Welcome" in res.data

def test_add_task(client):
    res = client.post("/tasks", json={"title": "Test Task"})
    assert res.status_code == 201
    assert res.json["title"] == "Test Task"

def test_get_tasks(client):
    client.post("/tasks", json={"title": "Another Task"})
    res = client.get("/tasks")
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_delete_task(client):
    client.post("/tasks", json={"title": "Task to delete"})
    res = client.delete("/tasks/1")
    assert res.status_code == 200
    assert res.json["message"] == "Task deleted"
