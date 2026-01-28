Project: CI/CD Automatisering met Jenkins & DockerIn dit laatste deel van het project wordt een volledige Continuous Integration & Deployment (CI/CD) pipeline opgezet om een Python-applicatie automatisch te implementeren en de status ervan te bewaken.

1. De Calculatie Applicatie (calc_app.py)Als onderdeel van een examenopdracht is een specifieke microservice ontwikkeld
2. :Functionaliteit: Een Flask-applicatie die een eenvoudige berekening uitvoert ($10 + 5$) en het resultaat samen met de status "Online" weergeeft.
3. :Poort: De applicatie is geconfigureerd om te draaien op poort 6060.
4.
5. 2. Geautomatiseerde Docker Build (launch_calc.sh)Om de container-omgeving consistent te houden, wordt gebruikgemaakt van een shellscript dat het Dockerfile dynamisch beheert:Resource Optimalisatie: Schakelt de progress-bar van pip uit om specifieke threading-fouten in Docker te voorkomen.Container Lifecycle: Stopt en verwijdert automatisch bestaande containers voordat een nieuwe versie wordt gebouwd en gestart op poort 6060.Automatisering: Genereert het Dockerfile "on the fly" tijdens de uitvoering.

   4. 3. Jenkins Pipeline Integratie (Jenkinsfile)De volledige flow is vastgelegd in een Jenkinsfile, die de stappen voor de Jenkins-agent definieert:Stage: Build & Deploy: Maakt het startscript uitvoerbaar (chmod +x) en voert dit uit om de nieuwste versie van de applicatie te lanceren.Stage: Health Check: Een cruciale stap waarbij via een curl-opdracht automatisch wordt gecontroleerd of de webserver een "200 OK" status teruggeeft. Dit garandeert dat de applicatie niet alleen draait, maar ook daadwerkelijk bereikbaar is.
