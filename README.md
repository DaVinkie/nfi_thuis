## Toelichting en Ervaringen NFI Opdracht - Daniël Vink

Na het doorlezen van de opdracht en het inrichten van mijn "werkomgeving" (venv, Git repo), besloot ik om eerst een
plan van aanpak voor alle onderdelen van de opdracht. De meeste van mijn keuzes zijn gebaseerd op de tools die ik in 
tijdens mijn huidige werkzaamheden ook gebruik. Voor het opzetten van de CI/CD pipeline koos ik echter om gebruik te
maken van GitHub Actions in plaats van Gitlab CI. Ik ging er vanuit dat de workflow van beiden relatief vergelijkbaar
zouden zijn en het leek me interessant om de verschillen te ontdekken.

#### CI/CD Pipeline en tests [1/2]
Voor de CI/CD Pipeline heb ik GitHub Actions gekozen omdat ik hier nog niet bekend mee ben. Bij mijn huidige werkgever
maken we gebruik van Gitlab en de bijhorende Gitlab CI functionaliteit. Het grootste verschil tussen beide is, naast het
vocabulair, dat GitHub Actions heel erg aanmoedigt om losse files te gebruiken in plaats van één centraal configuratie
bestand. Ook is de workflow net anders met beschikbare templates in de online GitHub omgeving. Zo vond ik er twee voor
Python apps en Docker files, en heb ik deze aan mijn project toegevoegd.

Om de CI/CD iets uit te laten voeren ben ik verder gegaan met het schrijven van tests. Hiervoor koos ik de pytest module,
omdat ik hier het meeste ervaring mee heb en deze goed geïntegreerd is in de PyCharm IDE. Ik begon met een aantal unit 
tests om functionaliteit uit domain.py te testen. Toen ik aan de integratie tests wilde beginnen, bedacht ik me dat het 
handiger was om eerst de app om te schrijven tot een API.

#### API
Als API Framework koos ik voor **FastAPI** omdat ik hier al eerder mee heb gewerkt en ik fan ben van de eenvoudigheid en 
ingebouwde /docs documentatie. Eerst heb ik een aantal kleine functies geschreven met mogelijke extra functionaliteit en
die een API endpoint gegeven. Daarna besloot ik de _grote_ `profiel_past_in_spoor` functie aan te passen met wat extra 
input controle. De main applicatie functie heb ik voor het gemak uitgecomment. Nadat de API naar behoren functioneerde
ben ik verder gegaan met het schrijven van de integratie tests.

#### CI/CD Pipeline en tests [2/2]
Voor de integratie tests heb ik gebruik gemaakt van de ingebouwde TestClient van FastAPI om een test-app op te starten 
waarvan ik zowel de output als de HTTP response codes kon controleren. Om daarna een tijdrapportage te kunnen maken heb
gebruik gemaakt van de pytest-benchmark extensie. Ik heb het project een kleine structuur refactor gegeven zodat de
verschillende type tests in verschillende stappen van de CI/CD pipeline uitgevoerd kunnen worden.

Voor het algehele project maak ik gebruik van **Poetry**, een tool voor het onderhouden van virtuele omgevingen en het
distributeren van python packages. Poetry maakt gebruik van de pyproject.toml waarin je heel netjes onderscheid kan
maken van je project dependencies - in plaats van losse requirement-bestanden te onderhouden. Ook kun je hierin je
configuratie bijhouden van andere tools, zoals bijvoorbeeld Ruff, of een source folder voor pytest.

#### Code checks
Omdat ik toch bezig was met de Pipeline besloot ik hier gelijk code controle aan toe te voegen in de vorm van **Ruff**. Ruff
is een linter en formatter op basis van Rust die hetzelfde functioneert als de klassiekers Black, mypy en flake8 maar dan
veel sneller. Ik maak veel gebruik van ruff tijdens het ontwikkelen, vaak als onderdeel van een .pre-commit bestand.

#### Dockerfile
De docker file die ik heb gemaakt is eigenlijk heel basic. Ik liep tegen een kleine worsteling aan omdat ik gebruik maak
van Poetry. Het installeren van binaries in een image leverde problemen op met permissions voor de lokale gebruiker die
ik aanmaakte voor de veiligheid. Dit probleem heb ik uiteindelijk op kunnen lossen door pas na het installeren van de 
dependencies te wisselen naar de lokale gebruiker.

Door het forwarden van ports in het `docker run` commando kon ik de API goed bereiken. Ik heb echter geen repository om
de image naar toe te pushen of een server/container om de image op te hosten opgezet in de CICD, dus dit zou je lokaal 
moeten draaien om dat te bevestigen. 



