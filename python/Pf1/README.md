Project: Python Debugging & Multi-Port Flask Services
In dit onderdeel wordt gedemonstreerd hoe verschillende Flask-microservices naast elkaar kunnen draaien door middel van specifieke poorttoewijzingen en hoe veelvoorkomende syntaxfouten in Python worden opgelost.

1. Python Debugging & Syntax Correctie
Een essentieel onderdeel van dit project was het identificeren en herstellen van een kritieke fout in het opstartscript van de applicatie:

Probleem: De applicatie startte niet op vanwege een foutieve syntax bij de if __name__ == "__main__": check.

Oplossing: De code is gecorrigeerd door de ontbrekende underscores toe te voegen, waardoor de webserver correct initialiseert wanneer het script direct wordt uitgevoerd.

Status Bevestiging: Na de fix geeft deze specifieke service de boodschap "Pf1 werkt!" terug op poort 5051.

2. Microservice Isolatie (Poortbeheer)
Om conflicten te vermijden en verschillende testomgevingen tegelijkertijd te faciliteren, zijn de Flask-services over verschillende poorten verdeeld:

Service A (Debugging): Draait op poort 5051.

Service B (Jenkins Validatie): Draait op poort 5050.

Stabiliteit: Beide services hebben threaded=False geconfigureerd in de app.run() methode om stabiliteitsproblemen in Docker- of Jenkins-omgevingen te voorkomen.

3. Netwerk- en Hostconfiguratie
Voor alle Python-services geldt een uniforme netwerkinstelling:

Host: Ingesteld op 0.0.0.0, wat cruciaal is voor containerisatie omdat de service hierdoor bereikbaar is van buiten de container (bijvoorbeeld via de hostmachine of de Jenkins-agent).
