Project: Flask Applicatie Containerisatie met Docker
Dit onderdeel van het project demonstreert het verpakken van een op maat gemaakte Python-webapplicatie in een Docker-container voor consistente implementatie.

1. Python Flask Applicatie (mijn_app.py)
De kern van de applicatie is een lichtgewicht webserver gebouwd met het Flask-framework:

Functionaliteit: De app rendert een index.html template en geeft de huidige systeemtijd door naar de frontend.

Configuratie: De server luistert op poort 7000 en is toegankelijk via alle netwerkinterfaces (0.0.0.0).

2. Docker Configuratie (Dockerfile)
Het Dockerfile bevat de blauwdruk voor het bouwen van de applicatie-image:

Basis Image: Maakt gebruik van de officiële python:3.9-slim image voor een minimale voetafdruk.

Werkmap: Stelt /app in als de actieve directory binnen de container.

Dependencies: Installeert automatisch het flask pakket via pip.

Poort Expositie: Stelt poort 7000 open voor verkeer naar de container.

Startcommando: Start de applicatie automatisch op bij het opstarten van de container.

3. Automatiseringsscript (deploy.sh)
Om het bouw- en implementatieproces te versnellen, is een Bash-script toegevoegd dat de volgende stappen automatiseert:

Opschonen: Stopt en verwijdert eventuele oude containers met dezelfde naam (mijn_examen_container) om fouten te voorkomen.

Build: Bouwt een nieuwe Docker-image genaamd mijn_examen_image op basis van de huidige directory.

Run: Start de container op de achtergrond (-d), koppelt poort 7000 van de host aan poort 7000 van de container, en geeft de container uitgebreide privileges.

Verificatie: Toont de status van de container en geeft de URL (http://localhost:7000) weer voor directe controle.
