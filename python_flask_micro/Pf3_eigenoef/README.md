Project: Bare Metal Microservice Management (Pf3)
Dit onderdeel van het project demonstreert het beheer van een microservice op "Bare Metal" niveau (rechtstreeks op de VM), inclusief procesbeheer en geautomatiseerde deployment via shell-scripts.

1. Systeem Microservice (system_service.py)
Er is een specifieke service ontwikkeld die systeem-informatie blootstelt via een API:

Endpoints:

Webpagina (/): Toont een visuele statusmelding dat de microservice actief is op poort 9000.

API Status (/status): Geeft een JSON-respons met technische details, zoals de service-naam, de huidige werkmap (os.getcwd()) en de bevestiging dat de app op "Bare Metal" draait (niet in een container).

Configuratie: De service draait op poort 9000 met threaded=False voor maximale stabiliteit binnen de examen-VM.

2. Geautomatiseerde Deployment (run_pf3.sh)
Om de microservice betrouwbaar te beheren, is een robuust Bash-script geschreven dat de volledige lifecycle controleert:

Proces Opschoning: Gebruikt pkill om oude actieve processen van de service te stoppen voordat een nieuwe versie wordt gestart.

Lokale Installatie: Installeert Flask specifiek voor de gebruiker (--user) en schakelt de pip progress-bar uit om thread-fouten tijdens de installatie te vermijden.

Background Execution: Gebruikt nohup om de microservice op de achtergrond te starten, waarbij alle logs worden opgeslagen in pf3.log voor latere inspectie.
