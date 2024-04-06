from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass
class GetCase:
    class Meta:
        name = "getCase"

    publication_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicationNumber",
            "type": "Element",
            "required": True,
            "pattern": r"([0-9]{2}\.){0,1}[a-z]{3}\.[0-9]{2}\.[0-9]{1,4}\.[F|S|R]\.[0-9]{4}\.[0-9]{1,2}\.[0-9]{2}",  # noqa: E501
        },
    )


class InstantieRechtbankCode(Enum):
    """
    :cvar VALUE_01: 's-Hertogenbosch 's-Hertogenbosch
    :cvar VALUE_02: Breda Breda
    :cvar VALUE_03: Maastricht Maastricht
    :cvar VALUE_04: Roermond Roermond
    :cvar VALUE_05: Arnhem Arnhem
    :cvar VALUE_06: Zutphen Zutphen
    :cvar VALUE_07: Zwolle-Lelystad Zwolle-Lelystad
    :cvar VALUE_08: Almelo Almelo
    :cvar VALUE_09: 's-Gravenhage 's-Gravenhage
    :cvar VALUE_10: Rotterdam Rotterdam
    :cvar VALUE_11: Dordrecht Dordrecht
    :cvar VALUE_12: Middelburg Middelburg
    :cvar VALUE_13: Amsterdam Amsterdam
    :cvar VALUE_14: Alkmaar Alkmaar
    :cvar VALUE_15: Haarlem Haarlem
    :cvar VALUE_16: Utrecht Utrecht
    :cvar VALUE_17: Leeuwarden Leeuwarden
    :cvar VALUE_18: Groningen Groningen
    :cvar VALUE_19: Assen Assen
    :cvar VALUE_40: Amsterdam Amsterdam
    :cvar VALUE_41: Noord-Holland Noord-Holland
    :cvar VALUE_42: Midden-Nederland
    :cvar VALUE_43: Noord-Nederland Noord-Nederland
    :cvar VALUE_44: Oost-Nederland Oost-Nederland
    :cvar VALUE_45: Den Haag Den Haag
    :cvar VALUE_46: Rotterdam Rotterdam
    :cvar VALUE_47: Limburg Limburg
    :cvar VALUE_48: Oost-Brabant Oost-Brabant
    :cvar VALUE_49: Zeeland-West-Brabant Zeeland-West-Brabant
    :cvar VALUE_50: Gelderland Gelderland
    :cvar VALUE_51: Overijssel Overijssel
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"


class SearchByDatePubType(Enum):
    """
    :cvar UITSPRAKEN_FAILLISSEMENT: Rulings on the commencement of
        bankruptcy procedures
    :cvar UITSPRAKEN_SCHULDSANERING: Rulings on the commencement of
        procedures on debt restucturing
    :cvar UITSPRAKEN_SURSEANCE: Rulings on the commencement of
        procedures on moratorium
    :cvar EINDE_FAILLISSEMENTEN: Rulings on the termination of
        bankruptcy procedures
    :cvar EINDE_SCHULDSANERINGEN: Rulings on the termination of
        procedures on  debt restucturing
    :cvar EINDE_SURSEANCES: Rulings on the termination of moratorium
    :cvar OVERIG: Other insolvency publications
    """

    UITSPRAKEN_FAILLISSEMENT = "Uitspraken faillissement"
    UITSPRAKEN_SCHULDSANERING = "Uitspraken schuldsanering"
    UITSPRAKEN_SURSEANCE = "Uitspraken surseance"
    EINDE_FAILLISSEMENTEN = "Einde faillissementen"
    EINDE_SCHULDSANERINGEN = "Einde schuldsaneringen"
    EINDE_SURSEANCES = "Einde surseances"
    OVERIG = "Overig"


@dataclass
class SearchModifiedSince:
    class Meta:
        name = "searchModifiedSince"

    modify_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "modifyDate",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SearchNaturalPerson:
    class Meta:
        name = "searchNaturalPerson"

    date_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dateOfBirth",
            "type": "Element",
            "required": True,
        },
    )
    prefix: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "max_length": 20,
        },
    )
    surname: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "max_length": 200,
        },
    )
    house_number: List[int] = field(
        default_factory=list,
        metadata={
            "name": "houseNumber",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    postal_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "max_occurs": 2,
            "length": 6,
            "pattern": r"[1-9][0-9]{3}[A-Z]{2}",
        },
    )


@dataclass
class SearchUndertaking:
    class Meta:
        name = "searchUndertaking"

    name: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "max_length": 200,
        },
    )
    commercial_register_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "commercialRegisterID",
            "type": "Element",
            "max_occurs": 2,
            "pattern": r"\d{5,8}",
        },
    )
    postal_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "max_occurs": 3,
            "length": 6,
            "pattern": r"[1-9][0-9]{3}[A-Z]{2}",
        },
    )
    house_number: List[int] = field(
        default_factory=list,
        metadata={
            "name": "houseNumber",
            "type": "Element",
            "max_occurs": 3,
        },
    )


@dataclass
class SearchByDate:
    class Meta:
        name = "searchByDate"

    date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    court: Optional[InstantieRechtbankCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    pub_type: List[SearchByDatePubType] = field(
        default_factory=list,
        metadata={
            "name": "pubType",
            "type": "Element",
            "max_occurs": 7,
        },
    )


@dataclass
class SearchInsolvencyId:
    class Meta:
        name = "searchInsolvencyID"

    insolvency_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "insolvencyID",
            "type": "Element",
            "required": True,
            "pattern": r"[F|S|R]\.(\d{2}/){0,1}\d{2}/\d{1,4}",
        },
    )
    court: Optional[InstantieRechtbankCode] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
