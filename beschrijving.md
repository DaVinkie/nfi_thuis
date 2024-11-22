
### DNA Profiling Applicatie - NFI Opdracht

**Introductie:**

Bij de telefonische screening heb je gewerkt met een script om een DNA profiel met een DNA spoor te vergelijken. 
Deze keer hebben we de code zelf opgeschoond en wat aangepast zodat de gebruiker zelf meerdere sequenties kan opgeven en op 'X' kan drukken om het programma te stoppen.
In deze opdracht werken we door met deze code om dieper in te gaan op jouw software engineering en DevOps vaardigheden. We zullen dus niet verder in gaan op de specifieke logica van de code.
We willen dat de code goed getest en gedraaid kan worden, zodat NFI collega's deze code kunnen gebruiken.
Hiervoor maken we gebruik van geautomatiseerde tests in een code repository om te zorgen dat de functionaliteit van de code niet verandert met aanpassingen. 
Ook zetten we de applicatie op als een Application Programming Interface (API) zodat andere applicaties eenvoudig de functionaliteit van DNA vergelijkingen kunnen gebruiken.

**Benodigdheden:**
- Installatie van Python en Docker op je lokale machine.

**Stappen:**
1. **Configureer een CI/CD Pipeline:**
   Zet een automatische test- en tijdrapportage-pipeline op in GitHub of GitLab. Zorg dat je een aantal delen van de code automatisch test (je hoeft dus niet alles te testen!), en draai een 'integratietest' waarbij je een tijdrapportage maakt van de performance van de code.

2. **Zet de applicatie op als een API:**
   Gebruik de bestaande code en een [API Framework](https://www.geeksforgeeks.org/top-python-rest-api-frameworks/#top-10-python-rest-api-frameworks-in-2024)* om de applicatie in een API te converteren. 
   Zorg dat de API een (valide) input kan ontvangen en een output teruggeeft die vertelt of de vergelijking tussen spoor en profiel succesvol was.

   \* Als je nog weinig/geen ervaring hebt is FastAPI het makkelijkste om mee te beginnen.
   <br><br>

**Bonus:**
- Schrijf een Dockerfile waarin je de API en andere code kopieert, en die bij het starten hetzelfde werkt als de API van Stap 2.
- Breid de CI/CD pipeline uit met code kwaliteit checks (denk bijvoorbeeld aan black, mypy of flake8).

**Inleveren:**
- Upload je code en configuratiebestanden naar een persoonlijke repository.
- Voeg een README toe met uitleg over je keuzes en ervaringen tijdens de opdracht.
- Stuur minstens een dag (24h) voor je gesprek bij ons op kantoor je code in een .zip of de link naar je repository.

Tijdens het sollicitatiegesprek zullen we je vragen om de oplossingen die je hebt gemaakt te presenteren. Veel succes!
