Project: Geavanceerde Jenkins Orchestratie & Multi-App Deployment
Dit onderdeel demonstreert het gebruik van Jenkins voor het beheren van complexe build-workflows, inclusief foutafhandeling en de integratie van meerdere microservices.

1. Jenkins Workflow & Foutafhandeling (Jenkinsfile)
Er is een robuuste pipeline opgezet die de volledige levenscyclus van een applicatie beheert:

Preparation Stage: Gebruikt een catchError blok om bestaande containers (samplerunning) veilig te stoppen en te verwijderen zonder de pipeline te laten crashen bij een eerste run.

Modulariteit: De pipeline roept andere Jenkins-jobs aan (BuildFlaskAppJob en TestFlaskAppJob) om een duidelijke scheiding van taken te behouden.

2. Dynamische Workspace Management (launch_sample.sh)
Voor de sample_app is een uitgebreid deployment-script ontwikkeld:

Opschonen: Verwijdert oude mappen (tempdir) en actieve containers om een schone lei te garanderen.

Workspace Structuur: Maakt automatisch de benodigde directory-structuur aan (templates en static) en kopieert de juiste bestanden naar de tijdelijke build-omgeving.

Veilige Docker Build: Genereert een Dockerfile die specifiek is geoptimaliseerd voor Python-omgevingen door pip-waarschuwingen en de progress-bar uit te schakelen om thread-fouten te voorkomen.

3. Sample Flask Applicatie (sample_app.py)
Een tweede microservice is toegevoegd om de Jenkins-integratie te valideren:

Status Bevestiging: De applicatie geeft de simpele boodschap "J1_jenkins: In orde!" terug bij benadering.

Stabiliteit: Om crashes in container-omgevingen te voorkomen, is threading expliciet uitgeschakeld (threaded=False).

Netwerk: De server is geconfigureerd om te luisteren op poort 5050.
