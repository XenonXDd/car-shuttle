import requests

BASE_URL = "http://127.0.0.1:8000"

# Test registering a passenger
passenger_data = {
    "id": "alice",
    "username": "securepass",
    "password": "passenger123"
}
passenger_response = requests.post(f"{BASE_URL}/register-passenger", json=passenger_data)
print("Passenger registration:", passenger_response.json())

# Test registering a driver
driver_data = {
    "id": "bob",
    "username": "driversecret",
    "password": "driver456"
}
driver_response = requests.post(f"{BASE_URL}/register-driver", json=driver_data)
print("Driver registration:", driver_response.json())

# Optional: Get driver info
driver_info = requests.get(f"{BASE_URL}/driver-info/{driver_data['id']}")
print("Driver info:", driver_info.json())

# Optional: Get passenger info
passenger_info = requests.get(f"{BASE_URL}/passenger-info/{passenger_data['id']}")
print("Passenger info:", passenger_info.json())
