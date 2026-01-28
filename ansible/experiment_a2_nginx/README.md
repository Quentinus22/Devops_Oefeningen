Project: Nginx Webserver Experiment & Configuratie
Dit deel van het project richt zich op het opzetten van een Nginx webserver als alternatief, inclusief specifieke serverinstellingen en globale Ansible-optimalisaties.

1. Globale Ansible Instellingen (ansible.cfg)
Om de uitvoering van playbooks soepeler te laten verlopen, is een configuratiebestand toegevoegd met de volgende standaardinstellingen:

Inventory: Verwijst automatisch naar het ./hosts bestand.

Host Key Checking: Uitgeschakeld (False) om SSH-bevestigingen te omzeilen bij nieuwe verbindingen.

Retry Files: Uitgeschakeld (False) om te voorkomen dat er .retry bestanden worden aangemaakt bij een mislukte run.

2. Nginx Webserver Playbook
Dit playbook automatiseert de overstap van Apache naar Nginx op de lokale machine:

Conflictpreventie: Stopt eerst de apache2 service om poortconflicten te vermijden, waarbij fouten worden genegeerd als Apache niet aanwezig is (ignore_errors: yes).

Nginx Installatie: Installeert de nieuwste versie van nginx en ververst de pakketlijsten (update_cache: yes).

Poortconfiguratie: Gebruikt lineinfile om de standaard Nginx-configuratie aan te passen zodat de server luistert op poort 8808 in plaats van poort 80.

Custom Home Page: Maakt een specifieke "Challenge Home Page" aan in /var/www/html/index.html.

Handlers: Bevat een notificatie (notify) om de Nginx-service te herstarten zodra de configuratie is gewijzigd.

3. Inventory (hosts)
De inventory definieert de groep [webservers] waarbij de lokale machine wordt gebruikt:

Host: localhost.

Connectie: Directe lokale uitvoering via ansible_connection=local.
