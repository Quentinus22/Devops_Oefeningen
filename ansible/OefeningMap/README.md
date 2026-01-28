Oefening – Apache Webserver Automatisatie met Ansible
Doel
Het automatiseren van de installatie en configuratie van een Apache webserver op een Linux-systeem. Hierbij wordt gebruikgemaakt van Infrastructure as Code (IaC) principes om een gepersonaliseerde HTML-pagina te genereren.

Gebruikte Tools
Ansible: Voor het automatiseren van de serverconfiguratie.

Apache2: De webserver software.

Jinja2: Voor het dynamisch genereren van de index.html pagina.

Bestanden in deze opdracht
playbook.yml: Bevat de automatiseringstaken (update, installatie, service beheer).

inventory: Definieert de doelgroep (webservers) en de verbindingstype.

index.html.j2: De template voor de landingspagina met variabele data.

Configuratie Details
Inventory (hosts) De automatisering wordt uitgevoerd op de lokale machine (localhost) onder de groep webservers.

Ini, TOML
[webservers]
localhost ansible_connection=local
Playbook Taken Het playbook voert de volgende acties uit met sudo (root) rechten:

Update apt cache: Zorgt dat de nieuwste pakketlijsten beschikbaar zijn.

Installeer Apache2: Installeert de webserver via de package manager.

Service Management: Start de Apache service en zorgt dat deze automatisch opstart na een reboot.

Template Deployment: Plaatst een gepersonaliseerde index.html in de webmap /var/www/html/.

Gebruik
Om het playbook uit te voeren, gebruik je het volgende commando in de terminal:

Bash
ansible-playbook -i inventory playbook.yml --ask-become-pass
Resultaat
Na uitvoering is de webserver bereikbaar op http://localhost. De gegenereerde pagina bevat:

De huidige datum (automatisch opgehaald via ansible_date_time).

De naam van de student (Quentin).

Een embedded Google Map van Dilbeek.
