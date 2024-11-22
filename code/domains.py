import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import StrEnum, Enum
from functools import cache
from typing import Tuple, Pattern, AnyStr


class NucleotideBase(StrEnum):
    A = "A"
    T = "T"
    C = "C"
    G = "G"

    @classmethod
    @cache
    def string_of_nucleotides(cls) -> str:
        return "".join(nucleotide for nucleotide in cls)


class IupacNucleotideCodeBase(Tuple, Enum):
    A = (NucleotideBase.A,)
    T = (NucleotideBase.T,)
    C = (NucleotideBase.C,)
    G = (NucleotideBase.G,)
    W = (NucleotideBase.A, NucleotideBase.T)
    S = (NucleotideBase.C, NucleotideBase.G)
    M = (NucleotideBase.A, NucleotideBase.C)
    K = (NucleotideBase.G, NucleotideBase.T)
    R = (NucleotideBase.A, NucleotideBase.G)
    Y = (NucleotideBase.C, NucleotideBase.T)
    B = (NucleotideBase.C, NucleotideBase.G, NucleotideBase.T)
    D = (NucleotideBase.A, NucleotideBase.G, NucleotideBase.T)
    H = (NucleotideBase.A, NucleotideBase.C, NucleotideBase.T)
    V = (NucleotideBase.A, NucleotideBase.C, NucleotideBase.G)
    N = (NucleotideBase.A, NucleotideBase.C, NucleotideBase.G, NucleotideBase.T)

    @classmethod
    @cache
    def iupac_sequentie_patroon(cls) -> str:
        return "".join(iupac.name for iupac in cls)

    def matched_nucleotide_base(self, nucleotide: NucleotideBase):
        if nucleotide in self.value:
            return True
        else:
            return False


@dataclass
class Sequentie(ABC):
    sequentie: str

    @classmethod
    @cache
    @abstractmethod
    def _pattern(cls) -> Pattern[AnyStr]:
        pass

    @classmethod
    @cache
    def _allowed_chars(cls):
        return re.sub(r"\W+", "", cls._pattern().pattern)

    def __post_init__(self):
        self._validate_sequentie()

    def _validate_sequentie(self):
        if not self._pattern().match(self.sequentie):
            raise ValueError(
                f"Een {type(self).__name__} mag alleen bestaan uit:"
                f"{self._allowed_chars()}\n"
                f"Opgeven sequentie: {self.sequentie}"
            )


@dataclass
class DNASpoor(Sequentie):
    """Een DNA spoor is een sequentie van IUPAC code karakters (en nucleotiden)"""

    @classmethod
    @cache
    def _pattern(cls):
        return re.compile(
            f"^[{''.join(iupac_char.name for iupac_char in IupacNucleotideCodeBase)}]*$"
        )


@dataclass
class DNAProfiel(Sequentie):
    """Een DNA profiel is een sequentie van nucleotiden"""

    @classmethod
    @cache
    def _pattern(cls):
        return re.compile(
            f"^[{''.join(nucleotide for nucleotide in NucleotideBase)}]*$"
        )
