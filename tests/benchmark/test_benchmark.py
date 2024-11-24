from fastapi.testclient import TestClient

from sequences.domains import DNAProfiel, DNASpoor, IupacNucleotideCodeBase
from sequences.main import app

client = TestClient(app)


def create_classes_for_benchmark():
    profiel = DNAProfiel("ACTG")
    patroon = IupacNucleotideCodeBase.iupac_sequentie_patroon()
    spoor = DNASpoor(patroon)
    return profiel, patroon, spoor


def test_create_classes_for_benchmark(benchmark):
    profiel, patroon, spoor = benchmark(create_classes_for_benchmark)
    assert profiel.sequentie == "ACTG"
    assert spoor.sequentie == patroon


def iupac_nucleotides_match():
    for iupac in IupacNucleotideCodeBase:
        for nuc in iupac.value:
            assert iupac.matched_nucleotide_base(nuc)
    return True


def test_iupac_nucleotides_match_benchmark(benchmark):
    result = benchmark(iupac_nucleotides_match)
    assert result


def get_profiel_past_in_spoor():
    response = client.get("app/past_in/TGATAC/YBATVN")
    return response.json()


def test_profiel_past_in_spoor_benchmark(benchmark):
    result = benchmark(get_profiel_past_in_spoor)
    assert result["profiel_past_in_spoor"]
