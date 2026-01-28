Project: Beveiligd Toegangsportaal & Dashboard (Pf2)
Dit onderdeel van het project focust op het creëren van een beveiligde gateway voor het systeemdashboard, waarbij gebruik wordt gemaakt van gebruikersvalidatie en foutafhandeling.

1. Authenticatie Logica (portaals_toegang)
De applicatie bevat een specifieke route die zowel GET (voor het tonen van de pagina) als POST (voor het verwerken van gegevens) verzoeken afhandelt:

Inloggegevens: Er zijn unieke, hardcoded inloggegevens ingesteld voor het examen:

Gebruiker: examen_user

Wachtwoord: DevNet2026

Validatie: Bij een correcte combinatie krijgt de gebruiker de status "Geautoriseerd" en toegang tot het Pf2 Dashboard.

Foutafhandeling: Indien de gegevens onjuist zijn, genereert het systeem een specifieke foutmelding: "Toegang geweigerd: Ongeldige ID of Sleutel".

2. Systeemoptimalisatie & Stabiliteit
Om de applicatie betrouwbaar te laten draaien binnen een virtuele machine (VM) of containeromgeving, zijn specifieke runtime-instellingen toegepast:

Poortbeheer: Deze service draait op poort 5056.

Threading: De optie threaded=False is expliciet geactiveerd, wat essentieel is om instabiliteit en crashes te voorkomen in beperkte VM-omgevingen.

Netwerk: Net als de andere services is deze geconfigureerd op 0.0.0.0 voor universele bereikbaarheid.
