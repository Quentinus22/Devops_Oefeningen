import requests
import json

BASE_URL = "http://library.demo.local/api/v1"
USER = "cisco"
PASS = "Cisco123!"

print("--- STAP 2: Boek bekijken ---")

# 1. Authenticatie
auth_response = requests.post(f"{BASE_URL}/loginViaBasic", auth=(USER, PASS))
token = auth_response.json()['token']
headers = {"X-API-Key": token}

# 2. GET Request naar boek 150
response = requests.get(f"{BASE_URL}/books/150", headers=headers)

if response.status_code == 200:
    print("✅ Boek gevonden:")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"❌ Fout bij ophalen ({response.status_code}): {response.text}")