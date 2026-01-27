import requests
import json

# Instellingen
BASE_URL = "http://library.demo.local/api/v1"
USER = "cisco"
# Let op: Als Cisco123! niet werkt, probeer dan cisco_123!
PASS = "Cisco123!" 

print("--- STAP 1: Boek toevoegen ---")

# 1. Authenticatie (Token ophalen)
print("Inloggen via Basic Auth...")
try:
    auth_response = requests.post(f"{BASE_URL}/loginViaBasic", auth=(USER, PASS))
    # Check of login lukte
    auth_response.raise_for_status() 
    token = auth_response.json()['token']
    print("✅ Token ontvangen!")
except Exception as e:
    print(f"❌ Login mislukt: {e}")
    exit()

# 2. Het boek toevoegen
headers = {"Content-Type": "application/json", "X-API-Key": token}

nieuw_boek = {
    "id": 150,
    "title": "oefening python",
    "author": "Quentin",
    "isbn": "9781234567897"
}

print(f"Boek {nieuw_boek['id']} aanmaken...")
response = requests.post(f"{BASE_URL}/books", headers=headers, json=nieuw_boek)

print(f"Status Code: {response.status_code}")
print(f"Antwoord server: {response.text}")