Project: MariaDB Database Server & Ansible Optimalisatie
Dit deel van het project automatiseert de inrichting van een MariaDB database-omgeving en stroomlijnt de workflow via een centraal configuratiebestand.

1. Database Server Experiment (A3 - Database Server Experiment)
Dit playbook configureert een volledige SQL-omgeving op de doelsystemen:

Installatie & Beheer:

Installeert de nieuwste versie van MariaDB Server via de apt-pakketbeheerder.

Zorgt dat de mariadb service actief is en automatisch opstart bij een systeemreboot.

Installeert de python3-mysqldb library, die noodzakelijk is voor Ansible om MySQL/MariaDB modules te kunnen aansturen.

Database Configuratie:

Maakt een nieuwe database aan met de naam GlineurQuentin_db.

Maakt een databasegebruiker aan genaamd devuser met het wachtwoord Cisco123!.

Kent volledige rechten (ALL) toe aan devuser voor de specifieke database.

Maakt gebruik van de login_unix_socket voor veilige lokale authenticatie.

2. Ansible Omgevingsinstellingen (ansible.cfg)
Om de efficiëntie te verhogen en handmatige handelingen te beperken, worden de volgende instellingen gehanteerd:

Inventory: Staat standaard ingesteld op ./hosts, zodat je dit niet telkens hoeft mee te geven in de opdrachtregel.

Host Key Checking: Staat op False, waardoor Ansible niet handmatig om bevestiging vraagt bij het verbinden met (nieuwe) servers.

Retry Files: Uitgeschakeld (False) om je projectmap schoon te houden van tijdelijke foutbestanden.

3. Inventory Beheer (hosts)
Er is een specifieke scheiding aangebracht in de servergroepen:

[dbservers]: Bevat de localhost voor de database-taken, waarbij gebruik wordt gemaakt van een directe lokale verbinding (ansible_connection=local).

[webservers]: Bevat de localhost voor web-gerelateerde taken.
