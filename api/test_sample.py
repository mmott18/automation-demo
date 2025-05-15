import requests

BASE_URL = "https://reqres.in/api"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

# def test_create_user():
#     payload = {"name": "matt", "job": "qa engineer"}
#     response = requests.post(f"{BASE_URL}/users", json=payload)
#     assert response.status_code == 201
#     assert "id" in response.json()

def test_update_user():
    payload = {"name": "matthew", "job": "senior qa engineer"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["job"] == "senior qa engineer"

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204

def test_register_unsuccessful():
    payload = {"email": "sydney@fife"}
    response = requests.post(f"{BASE_URL}/register", json=payload)
    assert response.status_code == 400
    assert "error" in response.json()

def test_register_successful():
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(f"{BASE_URL}/register", json=payload)
    assert response.status_code == 200
    assert "id" in response.json() and "token" in response.json()
