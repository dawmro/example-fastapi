import pytest
from jose import jwt
from app import schemas

from app.config import settings





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


@pytest.mark.parametrize("email, password, status_code", [
    ('wrongEmail@gmail.com', 'password123', 403),
    ('dawmro@gmail.com', 'wrongPassword', 403),
    ('wrongEmail@gmail.com', 'wrongPassword', 403),
    (None, 'password123', 422),
    ('dawmro@gmail.com', None, 422),
    (None, None, 422)
])
def test_incorrect_login(client, test_user, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == "Invalid Credentials"

