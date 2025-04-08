import requests

BASE_URL = "https://fakestoreapi.com"


def test_login_success():
    url = f"{BASE_URL}/auth/login"
    payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert "token" in response.json()


def test_login_failure():
    url = f"{BASE_URL}/auth/login"
    payload = {
        "username": "invalid_user",
        "password": "wrong_password"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 401  # Unauthorized
