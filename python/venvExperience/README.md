Project: Flask Applicatie-Isolatie via Virtuele Omgevingen
Dit onderdeel van het project demonstreert hoe een Flask-applicatie veilig en geïsoleerd van het hoofdsysteem kan worden gedraaid binnen een Virtual Environment (venv). Dit voorkomt conflicten tussen verschillende Python-projecten.

1. Applicatie-isolatie (venvExperience)
De applicatie is ondergebracht in een specifieke mapstructuur (python/venvExperience/app.py), wat wijst op een gestructureerde werkomgeving:

Environment: Gebruik van een lokale virtuele omgeving om bibliotheken zoals Flask te beheren zonder het globale systeem te belasten.

Requirements: De aanwezigheid van een requirements.txt bestand zorgt ervoor dat de juiste versies van alle dependencies met één commando geïnstalleerd kunnen worden.

2. Flask Service Configuratie
De service zelf is geoptimaliseerd voor een lokale ontwikkelomgeving:

Feedback: De applicatie geeft een duidelijke statusmelding terug: "Succes! Je Flask-app draait in venvExperience".

Poortconfiguratie: Deze specifieke instantie is toegewezen aan poort 4000.

Debug Mode: De server draait met debug=True, wat essentieel is tijdens de ontwikkelfase voor het live herladen van code en uitgebreide foutrapportage.
