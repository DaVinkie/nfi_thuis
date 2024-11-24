import pytest

from sequences.domains import DNAProfiel, DNASpoor, IupacNucleotideCodeBase, NucleotideBase


def test_dna_profiel_validate_invalid_char():
    with pytest.raises(ValueError):
        number = DNAProfiel("123")


def test_dna_profiel_validate_wrong_type():
    with pytest.raises(TypeError):
        number = DNAProfiel(123)
    with pytest.raises(TypeError):
        nested = DNAProfiel(DNAProfiel("ACTG"))


def test_dna_profiel_validate_spoor_input():
    with pytest.raises(ValueError):
        # Valid input for DNASpoor
        profiel = DNAProfiel("ACTGW")


def test_dna_profiel_correct_input():
    profiel = DNAProfiel("ACTG")
    assert profiel.sequentie == "ACTG"


def test_dna_spoor_correct_input():
    patroon = IupacNucleotideCodeBase.iupac_sequentie_patroon()
    spoor = DNASpoor(patroon)
    assert spoor.sequentie == patroon


def test_iupac_nucleotides_match():
    for iupac in IupacNucleotideCodeBase:
        for nuc in iupac.value:
            assert iupac.matched_nucleotide_base(nuc) == True


def test_iupac_nucleotides_not_match():
    assert not IupacNucleotideCodeBase.B.matched_nucleotide_base(NucleotideBase.A)
