import requests

BASE_URL = "https://fakestoreapi.com"


def test_add_to_cart():
    url = f"{BASE_URL}/carts"
    payload = {
        "userId": 1,
        "date": "2023-04-08",
        "products": [{"productId": 1, "quantity": 2}]
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200


def test_get_cart_by_user():
    url = f"{BASE_URL}/carts/user/1"
    response = requests.get(url)
    assert response.status_code == 200
