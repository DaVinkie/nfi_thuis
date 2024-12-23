"""
Deze code controleert of het DNA profiel van een persoon aanwezig
kan zijn in een DNA spoor dat gevonden is op een plaats delict.


Een DNA Profiel is een sequentie (e.g. ATTCGATTGATTAGCT) bestaande uit 4 verschillende nucleotide basen:
    A
    T
    C
    G
Een DNA spoor kan echter een mengprofiel zijn van meerdere personen, waardoor op sommige plekken meerdere nucleotiden
mogelijk zijn. Om de verschillende mogelijkheden weer te geven wordt er gebruik gemaakt van de zogeheten
'IUPAC nucleotide code' die bestaat uit de volgende karakters:
    R = A or G
    Y = C or T
    S = G or C
    W = A or T
    K = G or T
    M = A or C
    B = C or G or T
    D = A or G or T
    H = A or C or T
    V = A or C or G
    N = any nucleotide base


Om een voorbeeld te illustreren, vergelijken we de karakters van volgend DNA spoor met twee verschillende profielen.
DNA Spoor:          ATTCGWTTBATTVGCT
                         A  C   A
                         T  G   C
                            T   G
DNA Profiel:        ATTCGATTGATTAGCT    DNA profiel past in spoor
DNA Profiel:        ATTCGATTAATTAGCT    DNA profiel past niet in spoor
                            ^
"""  # noqa: E501

from fastapi import FastAPI, HTTPException

from sequences.domains import (
    DNAProfiel,
    DNASpoor,
    IupacNucleotideCodeBase,
    NucleotideBase,
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "User"}


@app.get("/nucleotides/bases")
def nucleotide_base():
    return {"bases": NucleotideBase.string_of_nucleotides()}


@app.get("/iupac/codes")
def iupac_codes():
    return {"iupac_codes": IupacNucleotideCodeBase.iupac_sequentie_patroon()}


@app.get("/iupac/nucleotides/{code}")
def iupac_nucleotides(code: str):
    try:
        result = IupacNucleotideCodeBase[code].value
    except KeyError as e:
        raise HTTPException(
            status_code=404, detail=f"Opgegeven code is niet geldig: {e}"
        ) from e
    return {"iupac_code": code, "iupac_nucleotides": result}


@app.get("/app/matcht/{nucleotide}/{code}")
def nucleotide_matcht_iupac_code(nucleotide: str, code: str):
    try:
        nuc = NucleotideBase(nucleotide)
        code_base = IupacNucleotideCodeBase[code]
    except KeyError as e:
        raise HTTPException(
            status_code=404, detail=f"Opgegeven nucleotide/code is niet geldig: {e}"
        ) from e

    if not code_base.matched_nucleotide_base(nuc):
        return {"nucleotide": nucleotide, "code": code, "matcht": False}
    return {"nucleotide": nucleotide, "code": code, "matcht": True}


@app.get("/app/past_in/{dna_profiel}/{dna_spoor}")
def profiel_past_in_spoor(dna_spoor: str, dna_profiel: str):
    try:
        spoor = DNASpoor(dna_spoor)
        profiel = DNAProfiel(dna_profiel)
    except (ValueError, TypeError) as e:
        raise HTTPException(
            status_code=404, detail=f"Opgegeven spoor voldoet niet aan vereisten: {e}"
        ) from e

    if len(profiel.sequentie) != len(spoor.sequentie):
        return {
            "dna_spoor": dna_spoor,
            "dna_profiel": dna_profiel,
            "profiel_past_in_spoor": False,
        }
    elif profiel.sequentie == spoor.sequentie:
        return {
            "dna_spoor": dna_spoor,
            "dna_profiel": dna_profiel,
            "profiel_past_in_spoor": True,
        }

    for i in range(len(profiel.sequentie)):
        profiel_base = NucleotideBase(profiel.sequentie[i])
        spoor_base = IupacNucleotideCodeBase[spoor.sequentie[i]]
        if not spoor_base.matched_nucleotide_base(profiel_base):
            return {
                "dna_spoor": dna_spoor,
                "dna_profiel": dna_profiel,
                "profiel_past_in_spoor": False,
            }
    return {
        "dna_spoor": dna_spoor,
        "dna_profiel": dna_profiel,
        "profiel_past_in_spoor": True,
    }


"""if __name__ == "__main__":
    stop_input = "X"
    nieuw_spoor_input = "SPOOR"

    stop_bool = False
    nieuw_spoor_bool = True

    print(f"Voer '{stop_input}' in om het programma te stoppen.")
    while not stop_bool:
        if nieuw_spoor_bool:
            user_input = input("Voer een sequentie voor het spoor in:").upper()
            try:
                dna_spoor = DNASpoor(user_input)
                nieuw_spoor_bool = False
            except ValueError as e:
                if user_input == stop_input:
                    print("Het programma sluit af...")
                    stop_bool = True
                else:
                    print(e)
                continue
            print(f"Voer '{nieuw_spoor_input}' in om een nieuw spoor op te geven.")

        user_input = input("Voer een sequentie voor het dna profiel in:").upper()
        try:
            dna_profiel = DNAProfiel(user_input)
            if profiel_past_in_spoor(dna_spoor, dna_profiel):
                print(f"\tHet DNA profiel past in spoor: {dna_spoor} vs {dna_profiel}")
            else:
                print(
                    f"\tHet DNA profiel past niet in spoor: {dna_spoor} vs {dna_profiel}"
                )
        except ValueError as e:
            if user_input == stop_input:
                print("Het programma sluit af...")
                stop_bool = True
            elif user_input == nieuw_spoor_input:
                nieuw_spoor_bool = True
            else:
                print(e)
            continue"""  # noqa: E501
