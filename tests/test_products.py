import json

import pytest
import requests

BASE_URL = "https://fakestoreapi.com"


def test_get_all_products():
    url = f"{BASE_URL}/products"
    response = requests.get(url)
    assert response.status_code == 200
    assert len(response.json()) > 0  # Ensure products exist


def test_get_product_by_id():
    url = f"{BASE_URL}/products/1"
    response = requests.get(url)
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == 1
    assert "title" in product


def test_invalid_product_id():
    url = f"{BASE_URL}/products/999999"  # Non-existent product ID
    response = requests.get(url)
    assert response.status_code == 404  # Not Found


def load_test_data():
    with open("data/test_data.json") as f:
        return json.load(f)


@pytest.mark.parametrize("data", load_test_data())
def test_product_titles(data):
    url = f"{BASE_URL}/products/{data['productId']}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["title"] == data["expectedTitle"]