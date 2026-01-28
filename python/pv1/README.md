Project: Interactieve Weather API Service
In dit onderdeel is een functionele webapplicatie ontwikkeld die fungeert als een interface voor weerinformatie. Het combineert dynamische HTML-formulieren met een gesimuleerde database-backend.

1. In-Memory "Database" Structuur
In plaats van een externe SQL-server, maakt deze applicatie gebruik van een Python dictionary (WEATHER_DB) om data op te slaan:

Data-inhoud: Bevat actuele weersinformatie (temperatuur en status) voor steden zoals Brussel, Antwerpen en Gent.

Structuur: Elke stad is gekoppeld aan een geneste dictionary, wat zorgt voor een snelle en efficiënte data-opvraging.

2. Frontend Integratie (HTML & Formulieren)
De applicatie bevat een geïntegreerde UI die rechtstreeks vanuit de Flask-code wordt geserveerd via render_template_string:

Gebruikersinterface: Een gecentreerde lay-out met een invoerveld waar gebruikers een stadsnaam kunnen typen.

Interactie: Maakt gebruik van een POST-methode om de ingevoerde data veilig naar de server te verzenden voor verwerking.

3. API Logica & JSON Respons
De backend is ontworpen volgens moderne API-standaarden:

Dataverwerking: De server ontvangt de stadsnaam, zet deze om naar kleine letters voor een betere match, en controleert of de stad in de database voorkomt.

Succes-respons: Indien gevonden, wordt de data teruggestuurd in JSON-formaat met een status success, inclusief de gekapitaliseerde stadsnaam en de weersgegevens.

Foutafhandeling: Indien een stad niet in de lijst staat, genereert de server een JSON-foutmelding (error) met de boodschap dat de stad niet gevonden is.
