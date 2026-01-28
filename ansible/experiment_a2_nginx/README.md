Doel
Dit experiment toont hoe met Ansible automatisch een Nginx webserver wordt geïnstalleerd en geconfigureerd op een specifieke poort (8808). Het playbook zorgt voor het stoppen van conflicterende diensten (Apache) en het aanmaken van meerdere HTML-pagina's met dynamische systeemgegevens zoals het IP-adres en de tijd.

Context
Omgeving: DEVASC VM / Localhost

Doel: De lokale machine (localhost)

Ansible connectie: Lokaal (connection: local)

Bestanden in deze map
hosts: Inventory bestand dat localhost definieert onder de groep [webservers].

ansible.cfg: Configuratiebestand voor lokale Ansible instellingen (zoals het uitschakelen van host_key_checking).

experiment_a2_nginx.yml: Het playbook dat de installatie, poortconfiguratie en pagina-creatie afhandelt.

README.md: Deze documentatie.

Wat doet het playbook?
Het playbook voert de volgende taken automatisch uit, zoals gedefinieerd in de broncode:

Stop Apache: Voorkomt poortconflicten door de apache2 service te stoppen (met ignore_errors voor het geval Apache niet aanwezig is).

Installeer Nginx: Installeert de nieuwste versie van Nginx en ververst de pakketlijsten.

Configureer Poort 8808: Wijzigt de standaard luisterpoort van 80 naar 8808 in het bestand /etc/nginx/sites-available/default.

Maak Challenge Home Page: Genereert een index.html met de initialen "GQ", het huidige IP-adres van de server en een tijdstempel.

Maak Map Page: Genereert een map.html met een geïntegreerde OpenStreetMap iframe.

Restart Nginx: Gebruikt een handler om de service te herstarten zodat de nieuwe poortinstellingen actief worden.

Playbook uitvoeren
Ga naar de juiste map in de terminal:

Bash
cd ~/labs/ansible/experiment_a2_nginx
Start het playbook met het volgende commando:

Bash
ansible-playbook -i hosts experiment_a2_nginx.yml --ask-become-pass
