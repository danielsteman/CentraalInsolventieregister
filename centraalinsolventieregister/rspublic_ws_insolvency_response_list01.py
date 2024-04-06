from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.rechtspraak.nl/namespaces/inspubber01"


class ExceptieCode(Enum):
    """
    :cvar VALUE_1: Geen resultaten gevonden No results found
    :cvar VALUE_2: Technische fout in de afhandeling van de request
        Technical error while handling the request
    :cvar VALUE_3: Te veel resultaten gevonden. Beperk de zoekvraag To
        many results. Limit your search
    :cvar VALUE_4: Input niet correct. Raadpleeg de handleiding.
        Incorrect input. Consult the manual.
    :cvar VALUE_5: Er kan niet worden gegarandeerd dat de gevraagde
        bestanden goed aansluiten. U dient een nieuw historie-bestand te
        downloaden. Raadpleeg de handleiding. It can not be garantueed
        that the requested records fit correctly for synchronization
        pruposes. You have to download a new history-file. Consult the
        manual.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


@dataclass
class PublicatieLijst:
    class Meta:
        name = "publicatieLijst"
        namespace = "http://www.rechtspraak.nl/namespaces/inspubber01"

    exceptie: Optional["PublicatieLijst.Exceptie"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publicatie_kenmerk: List[str] = field(
        default_factory=list,
        metadata={
            "name": "publicatieKenmerk",
            "type": "Element",
            "pattern": r"([0-9]{2}\.){0,1}[a-z]{3}\.[0-9]{2}\.[0-9]{1,4}\.[F|S|R]\.[0-9]{4}\.[0-9]{1,2}\.[0-9]{2}",  # noqa: E501
        },
    )
    extractiedatum: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Exceptie:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        errorcode: Optional[ExceptieCode] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
