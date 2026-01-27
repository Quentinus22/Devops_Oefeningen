import requests

BASE_URL = "http://library.demo.local/api/v1"
USER = "cisco"
PASS = "Cisco123!"

print("--- STAP 4: Boek verwijderen ---")

# 1. Authenticatie
auth_response = requests.post(f"{BASE_URL}/loginViaBasic", auth=(USER, PASS))
token = auth_response.json()['token']
headers = {"X-API-Key": token}

# 2. DELETE Request
response = requests.delete(f"{BASE_URL}/books/150", headers=headers)

print(f"Status Code: {response.status_code}")
if response.status_code in [200, 204]:
    print("✅ Boek 150 is verwijderd.")
else:
    print(f"❌ Verwijderen mislukt: {response.text}")