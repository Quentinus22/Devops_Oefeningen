Project: Gedistribueerde Microservices & Poortbeheer
Dit onderdeel rondt het portfolio af door te laten zien hoe meerdere onafhankelijke Python-services simultaan kunnen draaien binnen één ecosysteem door gebruik te maken van logische poortscheiding.

1. Flask Service Pf1:Oef1 (python_flask_micro/app.py)
Er is een specifieke oefening opgezet om de basisconnectiviteit van een microservice te valideren:

Functionaliteit: De service dient als een "Health Check" eindpunt en geeft de bevestiging "Pf1:Oef1 : In orde!" terug bij bezoek aan de root-URL.

Poortconfiguratie: Om poortconflicten met de andere services (zoals de Weather API of de Calc App) te vermijden, is deze service specifiek toegewezen aan poort 5055.

Netwerk Interface: De app is geconfigureerd op host='0.0.0.0', wat essentieel is voor bereikbaarheid binnen Docker-netwerken of externe netwerkvraagstukken.

2. DevOps Best Practices: Configuratie-overzicht
Doorheen het project zijn verschillende technieken toegepast om deze services stabiel te beheren:

Ansible Optimalisatie: Gebruik van een centraal ansible.cfg bestand om automatisch de juiste hosts inventory te laden en SSH-waarschuwingen (host_key_checking) te onderdrukken voor snellere uitrol.

Service Isolatie: Elke Python-app draait in zijn eigen context (Docker, venv of standalone), waarbij poortnummers fungeren als de unieke adressen binnen het project.
