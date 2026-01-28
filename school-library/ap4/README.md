Project: API Webformulier & Data Verwerking (Ap4)
Dit onderdeel van het project demonstreert de integratie tussen een frontend HTML-formulier en een backend API-endpoint voor het verwerken van gebruikersinvoer.

1. Interactieve Gebruikersinterface
Er is een gestileerd webformulier ontwikkeld met een moderne lay-out:

Input Velden: Gebruikers kunnen een gebruikersnaam (username) en een specifiek bericht (message) invoeren.

Styling: Het formulier is voorzien van embedded CSS voor een responsieve container-breedte, specifieke marges en een herkenbare blauwe actieknop.

Methodiek: Het formulier maakt gebruik van de POST-methode om data veilig te verzenden naar het /api/verwerk endpoint.

2. Backend API Logica
De Flask-server is geconfigureerd om de binnengekomen data direct te verwerken:

Route Management: Er zijn gescheiden routes voor het tonen van het formulier (GET) en het verwerken van de invoer (POST).

Dynamische Respons: De server is in staat om de verstuurde velden op te vangen en een bevestiging of JSON-respons terug te sturen naar de gebruiker.
