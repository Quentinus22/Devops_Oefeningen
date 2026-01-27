import requests
import json

BASE_URL = "http://library.demo.local/api/v1"
USER = "cisco"
PASS = "Cisco123!"

print("--- STAP 3: Boek updaten ---")

# 1. Authenticatie
auth_response = requests.post(f"{BASE_URL}/loginViaBasic", auth=(USER, PASS))
token = auth_response.json()['token']
headers = {"Content-Type": "application/json", "X-API-Key": token}

# 2. Data wijzigen (We passen de titel aan)
update_data = {
    "id": 150,
    "title": "oefening python (AANGEPAST)",
    "author": "Glenn",
    "isbn": "9781234567897"
}

# 3. PUT Request
response = requests.put(f"{BASE_URL}/books/150", headers=headers, json=update_data)

print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    print("✅ Update geslaagd!")
else:
    print(f"Antwoord server: {response.text}")