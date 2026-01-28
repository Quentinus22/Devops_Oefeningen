Project: Geautomatiseerde Apache Webserver Configuratie
Dit project maakt gebruik van Ansible om automatisch een Apache2 webserver te installeren, configureren en een dynamische landingspagina te publiceren op een doelsysteem.

Projectonderdelen
Het project bestaat uit drie hoofdbestanden:

Ansible Playbook (playbook.yml): Bevat de instructies voor de installatie en configuratie.

Inventory (hosts): Definieert op welke servers de taken moeten worden uitgevoerd (in dit geval de lokale machine).

Jinja2 Template (index.html.j2): Een dynamisch HTML-bestand dat variabelen gebruikt om informatie weer te geven.

Functionaliteiten
1. Systeembeheer & Installatie
Het playbook voert de volgende beheertaken uit met root-rechten (become: yes):

Update apt cache: Zorgt ervoor dat de pakketlijsten up-to-date zijn.

Apache2 Installatie: Installeert het apache2 pakket via de package manager.

Service Management: Start de Apache-dienst en zorgt ervoor dat deze automatisch opstart bij een reboot (enabled: yes).

2. Dynamische Content Generatie
In plaats van een statisch bestand, gebruikt dit project een Jinja2 template.

Locatie: Het bestand wordt geplaatst in /var/www/html/index.html.

Variabelen: De pagina toont automatisch de huidige datum van het systeem middels de Ansible fact: {{ ansible_date_time.date }}.

Inhoud: De pagina bevat de naam van de beheerder (Quentin) en een embedded Google Maps kaart van Dilbeek.

3. Infrastructuur als Code (IaC)
De configuratie is strikt gescheiden van de uitvoering:

De target host is ingesteld als localhost met een local verbindingstype, wat ideaal is voor testen of lokale webservers.

Bestandsrechten voor de indexpagina worden veilig ingesteld op 0644.

Hoe dit project te gebruiken
Zorg dat Ansible geïnstalleerd is op je systeem.

Voer het playbook uit met het volgende commando:

Bash
ansible-playbook -i hosts playbook.yml
Bezoek http://localhost in je browser om het resultaat te bekijken.
