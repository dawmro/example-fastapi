import pytest
from jose import jwt
from app import schemas
from .database import client, session
from app.config import settings


@pytest.fixture(scope="function")
def test_user(client):
    user_data={"email": "dawmro@gmial.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


def test_root(client):
    res = client.get("/")
    assert res.json().get("message") == "Hello World"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "hello123@gmial.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmial.com"
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, key = settings.secret_key, algorithms = [settings.algorithm])
    id: str = test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
