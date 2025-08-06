import requests

BASE_URL = "http://127.0.0.1:8000"

def test_get_passenger_info(passenger_id):
    url = f"{BASE_URL}/passenger-info/{passenger_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Passenger info retrieved successfully:")
        print(response.json())
    else:
        print(f"Failed to get passenger info. Status code: {response.status_code}, Detail: {response.json()}")

def test_get_driver_info(driver_id):
    url = f"{BASE_URL}/driver-info/{driver_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Driver info retrieved successfully:")
        print(response.json())
    else:
        print(f"Failed to get driver info. Status code: {response.status_code}, Detail: {response.json()}")

if __name__ == "__main__":
    # Replace these example IDs with actual IDs you have in your CSV files
    example_passenger_id = "alice"
    example_driver_id = "bob"

    print("Testing Passenger Info Endpoint")
    test_get_passenger_info(example_passenger_id)
    
    print("\nTesting Driver Info Endpoint")
    test_get_driver_info(example_driver_id)
