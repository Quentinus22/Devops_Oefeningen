Project: Webex Collaboration & Team Automatisering
In dit onderdeel wordt gedemonstreerd hoe Python wordt ingezet voor de automatische orchestratie van samenwerkingsruimtes binnen Cisco Webex. Dit script automatiseert het aanmaken van teams en het beheren van lidmaatschappen op basis van gestructureerde data.

1. API Authenticatie & Configuratie
Het script maakt gebruik van de officiële Webex REST API om acties uit te voeren:

Bearer Token: Er wordt gebruikgemaakt van een persoonlijk toegangs-token voor beveiligde communicatie met de Webex-omgeving.

Headers: Alle verzoeken zijn voorzien van de juiste Authorization en Content-Type headers om JSON-data uit te wisselen.

2. Gestructureerd Groepsbeheer
De automatisering wordt aangestuurd door een complexe dictionary-structuur (groups_struc):

Groepsidentificatie: Definieert unieke groepsnamen, zoals devasc_skills_Quentin.

Ledenbeheer: Bevat een lijst met teamleden inclusief namen en officiële studenten-e-mailadressen.

3. Geautomatiseerde Workflow
Het script voert een twee-staps proces uit voor elke gedefinieerde groep:

Ruimte aanmaken (Room Creation): Er wordt een POST-verzoek gestuurd naar /rooms om een nieuwe virtuele ruimte te creëren. Bij succes (status 200) wordt de unieke ID van de nieuwe ruimte opgeslagen.

Leden Toevoegen (Memberships): Het script loopt automatisch door de lijst met leden en stuurt voor elke persoon een POST-verzoek naar /memberships om hen met hun e-mailadres aan de zojuist gemaakte ruimte te koppelen.
