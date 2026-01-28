import requests
import json

# Je persoonlijke access token van developer.webex.com
access_token = "VERVANG_DIT_DOOR_JE_TOKEN"

# De structuur met groepen en members (gebaseerd op jouw voorbeeld)
groups_struc = {
    "groups": [
        { "group": { 
            "group_id": "G1", 
            "group_name": "devasc_skills_Quentinus",
            "members": [
                {"person_name": "Quentin", "email": "quentin.glineur@student.odisee.be"},
                {"person_name": "Yvan", "email": "yvan.rooseleer@biasc.be"}
            ]
          }
        }
    ]
}

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# 1. Maak de Ruimte (Room) aan
url_rooms = 'https://webexapis.com/v1/rooms'
for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["group_name"]
    print(f"Creating ... {create_group_name}")
    payload_space = {"title": create_group_name}
    res_space = requests.post(url_rooms, headers=headers, json=payload_space)
    
    if res_space.status_code == 200:
        NEW_SPACE_ID = res_space.json()["id"]
        
        # 2. Voeg Members toe aan de nieuwe ruimte
        url_members = 'https://webexapis.com/v1/memberships'
        for mbr in rec["group"]["members"]:
            person_email = mbr["email"]
            payload_member = {'roomId': NEW_SPACE_ID, 'personEmail': person_email}
            requests.post(url_members, headers=headers, json=payload_member)
            print(f"Member toegevoegd: {person_email}")

        # 3. Stuur het Bericht
        url_messages = 'https://webexapis.com/v1/messages'
        message_text = "Pf3 Microservice Experiment: Webex Integration succesvol!"
        payload_message = {'roomId': NEW_SPACE_ID, 'text': message_text}
        res_message = requests.post(url_messages, headers=headers, json=payload_message)

        if res_message.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Error sending message: {res_message.status_code}")