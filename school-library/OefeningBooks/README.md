Project: School Library Data Management
Dit onderdeel van het project richt zich op het programmatisch beheren van een boekencollectie. Het bevat scripts voor interactie met een database-backend en een module voor het genereren van grote hoeveelheden testdata.

1. CRUD Operaties (OefeningBooks)
Binnen de map school-library zijn specifieke Python-scripts ontwikkeld voor elke fase van databeheer:

Create (myscriptcreate.py): Voor het toevoegen van nieuwe boeken aan de bibliotheek-database.

Read (myscriptget.py): Voor het ophalen en raadplegen van bestaande boekgegevens.

Update (myscriptupdate.py): Voor het aanpassen van informatie van reeds aanwezige boeken.

Delete (myscriptdelete.py): Voor het veilig verwijderen van records uit de collectie.

2. Bulk Data Generatie
Om de prestaties en schaalbaarheid van de bibliotheek-app te testen, is een automatiseringsscript toegevoegd:

Mass-insert (add100RandomBooks.py): Dit script genereert automatisch 100 willekeurige boek-records en voegt deze in één keer toe aan de database. Dit is essentieel voor het testen van zoek- en sorteerfuncties binnen de API.
