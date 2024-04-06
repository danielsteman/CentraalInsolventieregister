from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://www.rechtspraak.nl/namespaces/inspubber01"


class ExceptieCode(Enum):
    """
    ExceptionCode.

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
class InspubAdresCbelem:
    class Meta:
        name = "inspubAdresCBElem"

    datum_begin: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "datumBegin",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
        },
    )
    straat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "max_length": 35,
        },
    )
    huisnummer: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
        },
    )
    huisnummer_toevoeging1: Optional[str] = field(
        default=None,
        metadata={
            "name": "huisnummerToevoeging1",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 10,
        },
    )
    huisnummer_toevoeging2: Optional[str] = field(
        default=None,
        metadata={
            "name": "huisnummerToevoeging2",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 10,
        },
    )
    postcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "length": 6,
            "pattern": r"[1-9][0-9]{3}[A-Z]{2}",
        },
    )
    plaats: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "max_length": 40,
        },
    )
    telefoonnummer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 15,
        },
    )


@dataclass
class InspubAdresInsolvente:
    """
    :ivar datum_begin:
    :ivar straat: Lengte in afwijking van NEN. Length not NEN-compliant.
    :ivar huisnummer: Lengte in afwijking van NEN Length not NEN-
        compliant.
    :ivar huisnummer_toevoeging1: Lengte in afwijking van NEN Length not
        NEN-compliant.
    :ivar huisnummer_toevoeging2: Bestaan en lengte in afwijking van NEN
        Existence and length not NEN-compliant.
    :ivar postcode:
    :ivar plaats: Lengte in afwijking van NEN. Nederlandse plaatsen
        worden gevuld via postcode-tabel. Length not NEN-compliant.
        Dutch geographical names names are taken from the postal code
        database.
    """

    class Meta:
        name = "inspubAdresInsolvente"

    datum_begin: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "datumBegin",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
        },
    )
    straat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "max_length": 35,
        },
    )
    huisnummer: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
        },
    )
    huisnummer_toevoeging1: Optional[str] = field(
        default=None,
        metadata={
            "name": "huisnummerToevoeging1",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 10,
        },
    )
    huisnummer_toevoeging2: Optional[str] = field(
        default=None,
        metadata={
            "name": "huisnummerToevoeging2",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 10,
        },
    )
    postcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "length": 6,
            "pattern": r"[1-9][0-9]{3}[A-Z]{2}",
        },
    )
    plaats: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 40,
        },
    )


class InspubAdresType(Enum):
    """
    Adress Type.

    :cvar WOON: Woonadres residential address
    :cvar VEST: Vestigingsadres Business address
    :cvar CORR: Correspondentieadres Postal address
    :cvar VRHN: Voorheen formerly
    :cvar PBAV: Aanvullende postblokkade additional mail blockade
    :cvar PBTI: Tussentijdse intrekking postblokkade interim abrogation
        mail blockade
    """

    WOON = "WOON"
    VEST = "VEST"
    CORR = "CORR"
    VRHN = "VRHN"
    PBAV = "PBAV"
    PBTI = "PBTI"


class InspubCbvCb(Enum):
    """
    CBV = Curator / bewindvoerder CBV = Administrator / Receiver.

    :cvar C: Curator Administrator (bankruptcy)
    :cvar B: Bewindvoerder Receiver (debt restructuring or mortuarium
        procedure)
    """

    C = "C"
    B = "B"


class InspubPublicatiesoortCode(Enum):
    """kind of publication - code

    :cvar VALUE_1200: uitspraak faillissement in cassatie op [datum
        handeling] declaration of bankruptcy in cassation proceedings on
        [date]
    :cvar VALUE_1201: faillissement van rechtswege door tussentijdse
        beëindiging schuldsanering in cassatie op [datum handeling]
        bankruptcy de jure as result of interim termination of debt
        restructuring in cassation on [date]
    :cvar VALUE_1202: vernietiging faillissement in cassatie op [datum
        handeling] nullification of bankruptcy in cassation on [date]
    :cvar VALUE_2200: uitspraak schuldsanering in cassatie op [datum
        handeling] admission to debt restructuring in cassation on
        [date]
    :cvar VALUE_2201: omzetting faillissement in schuldsanering in
        cassatie op [datum handeling] conversion of bankruptcy into debt
        restructuring in cassation on [date]
    :cvar VALUE_2202: herleving schuldsanering door vernietiging
        faillissement in cassatie op [datum handeling] resurgence of
        debt restructuring because of nullification of bankruptcy in
        cassation on [date]
    :cvar VALUE_3200: verlening definitieve surseance in cassatie op
        [datum handeling] Granting of final moratorium  in cassation on
        [date]
    :cvar VALUE_3201: behandeling cassatieberoep bij de hoge raad tegen
        afwijzing definitieve surseance op [datum handeling] om
        [tijdstip] proceedings on appeal to the Supreme Court on
        rejection of final admission to moratorium on [date] at [time]
    :cvar VALUE_3202: behandeling cassatieberoep tegen toewijzing
        definitieve surseance op [datum handeling] om [tijdstip]
        proceedings on appeal to the Supreme Court  on final admission
        to moratorium on [date] at [time]
    :cvar VALUE_1100: uitspraak faillissement in hoger beroep op [datum
        handeling] declaration of bankruptcy in appeal on [date]
    :cvar VALUE_1101: faillissement van rechtswege door tussentijdse
        beëindiging schuldsanering in hoger beroep op [datum handeling]
        bankruptcy de jure as result of interim termination of debt
        restructuring in appeal on [date]
    :cvar VALUE_1102: vernietiging faillissement in hoger beroep op
        [datum handeling] nullification of bankruptcy in appeal on
        [date]
    :cvar VALUE_2100: uitspraak schuldsanering in hoger beroep op [datum
        handeling] admission to debt restructuring in appeal on [date]
    :cvar VALUE_2101: omzetting faillissement in schuldsanering in hoger
        beroep op [datum handeling] conversion of bankruptcy into debt
        restructuring in appeal on [date]
    :cvar VALUE_2102: herleving schuldsanering door vernietiging
        faillissement in hoger beroep op [datum handeling] resurgence of
        debt restructuring because of nullification of bankruptcy in
        appeal on [date]
    :cvar VALUE_3100: verlening definitieve surseance in hoger beroep op
        [datum handeling] final admission to moratorium in appeal on
        [date]
    :cvar VALUE_3101: behandeling hoger beroep tegen afwijzing
        definitieve surseance op [datum handeling] om [tijdstip] hearing
        court of appeal on rejection of final admission to moratorium on
        [date] at [time]
    :cvar VALUE_3102: behandeling hoger beroep tegen toewijzing
        definitieve surseance op [datum handeling] om [tijdstip] hearing
        court of appeal on final admission to moratorium on [date] at
        [time]
    :cvar VALUE_3310: rectificatie rectification
    :cvar VALUE_1323: rectificatie rectification
    :cvar VALUE_2300: rectificatie rectification
    :cvar VALUE_1300: uitspraak faillissement op [datum handeling]
        declaration of bankruptcy on [date]
    :cvar VALUE_1301: uitspraak faillissement door tussentijdse
        beëindiging schuldsanering op [datum] declaration of bankruptcy
        as result of interim termination of debt restructuring on [date]
    :cvar VALUE_1302: uitspraak faillissement tijdens schuldsanering op
        [datum] declaration of bankruptcy during debt restructuring on
        [date]
    :cvar VALUE_1303: uitspraak faillissement door ontbinding akkoord in
        schuldsanering op [datum] declaration of bankruptcy by
        rescission of debt restructuring agreement on [date]
    :cvar VALUE_1304: heropening faillissement door ontbinding akkoord
        in faillissement op [datum] reopening bankruptcy by rescission
        of bankruptcy agreement on [date]
    :cvar VALUE_1305: uitspraak faillissement door ontbinding akkoord in
        surseance op [datum] declaration of bankruptcy by rescission of
        moratorium agreement on [date]
    :cvar VALUE_1306: uitspraak faillissement na beëindiging surseance
        op [datum] declaration of bankruptcy after termination of
        moratorium on [date]
    :cvar VALUE_2301: uitspraak schuldsanering op [datum uitspraak]
        admission to debt restructuring on  [date]
    :cvar VALUE_2302: uitspraak schuldsanering op [datum uitspraak] en
        verificatievergadering op [datum handeling] om [tijdstip]
        admission to debt restructuring on [date] and verification
        meeting on [date] at [time]
    :cvar VALUE_2303: uitspraak schuldsanering op [datum uitspraak]
        verificatievergadering met akkoordbehandeling op [datum
        handeling] om [tijdstip] admission to debt restructuring on
        [date] and verification meeting with hearing on agreement on
        [date] at [time]
    :cvar VALUE_2304: omzetting faillissement in schuldsanering op
        [datum uitspraak] conversion of bankruptcy into debt
        restructuring on [date]
    :cvar VALUE_2305: uitspraak schuldsanering na vernietiging
        faillissement door verzet op [datum uitspraak] admission to debt
        restructuring  after nullification of bankruptcy by opposition
        on [date]
    :cvar VALUE_2306: omzetting voorlopige surseance in schuldsanering
        op [datum uitspraak] conversion of provisional moratorium into
        debt restructuring on [date]
    :cvar VALUE_2307: uitspraak voorlopige schuldsanering op [datum
        uitspraak] provisional admission to debt restructuring on [date]
    :cvar VALUE_2308: omzetting voorlopige schuldsanering in definitieve
        op [datum handeling] conversion of provisonal admission to debt
        restructuring into a final admission on [date]
    :cvar VALUE_3300: verlening voorlopige surseance op [datum
        uitspraak] crediteurenvergadering op [datum uitspraak] om
        [tijdstip] admission to interim moratorium on [date] meeting of
        creditors on [date] at [time]
    :cvar VALUE_3301: verlening voorlopige surseance op [datum
        uitspraak]  crediteurenvergadering met akkoordbehandeling  op
        [datum uitspraak] om [tijdstip] admission to interim moratorium
        on [date] meeting of creditors with hearing on agreement on
        [date] at [time]
    :cvar VALUE_3302: verlening definitieve surseance bij beschikking
        van [datum handeling] met ingang van [datum uitspraak] voor de
        duur van [variabel maanden/ jaren] admission to final moratorium
        by order of [date] from [date] for the duration of [variable
        number of months / years]
    :cvar VALUE_3303: verlenging termijn van surseance bij beschikking
        van [datum handeling] met ingang van [datum variabel] voor de
        duur van [variabel maanden/jaren] extension of moratorium term
        by order of [date] from [date] for the duration of  [variable
        number of months / years]
    :cvar VALUE_1307: vervanging curator [naam oude cur] door [naam
        nieuwe cur] replacement of administrator [name former
        administrator] by [name new administrator]
    :cvar VALUE_2309: vervanging bewindvoerder [naam oude bwv] door
        [naam nieuwe bwv] replacement of receiver  [name former
        receiver] by [name new receiver]
    :cvar VALUE_3304: vervanging bewindvoerder [naam oude bwv] door
        [naam nieuwe bwv] replacement of receiver  [name former
        receiver] by [name new receiver]
    :cvar VALUE_1308: vereenvoudigde afwikkeling van het faillissement
        simplified bankruptcy proceedings
    :cvar VALUE_1309: verificatievergadering op [datum handeling] om
        [tijdstip] verification meeting on [date] at [time]
    :cvar VALUE_1310: verificatievergadering en akkoordbehandeling op
        [datum handeling] om [tijdstip] verification meeting and hearing
        on agreement on [date] at [time]
    :cvar VALUE_1311: vergadering van schuldeisers op [datum handeling]
        om [tijdstip] meeting of creditors on [date] at [time]
    :cvar VALUE_2310: verificatievergadering op [datum handeling] om
        [tijdstip] verification meeting on [date] at [time]
    :cvar VALUE_2311: verificatievergadering en akkoordbehandeling op
        [datum handeling] om [tijdstip] verification meeting and hearing
        on agreement on [date] at [time]
    :cvar VALUE_2312: verificatievergadering, saneringsplan en
        akkoordbehandeling op [datum handeling] om [tijdstip]
        verification meeting, plan of sanitation and hearing on
        composition on [date] at [time]
    :cvar VALUE_2313: voortzetting verificatievergadering, saneringsplan
        en akkoordbehandeling op [datum handeling] om [tijdstip]
        resumption of verification meeting, restructuring plan and
        hearing on agreement on [date] at [time]
    :cvar VALUE_2314: verificatievergadering en zitting wijziging
        saneringsplan op [datum handeling] om [tijdstip] verification
        meeting and hearing on adjustment of restructuring plan on
        [date] at [time]
    :cvar VALUE_2315: verificatievergadering en zitting beëindiging op
        [datum handeling] om [tijdstip] verification meeting and hearing
        on termination on [date] at [time]
    :cvar VALUE_2316: verificatievergadering en zitting beëindiging op
        [datum handeling] om [tijdstip]  neerlegging slotuitdelingslijst
        vanaf [datum variabel] verification meeting and hearing on
        termination on [date] at [time] deposition of final distribution
        list from [date]
    :cvar VALUE_2317: verificatievergadering en zitting wijziging
        saneringsplan en beëindiging op [datum handeling] om [tijdstip]
        verification meeting and hearing on adjustment of restructuring
        plan and termination on [date] at [time]
    :cvar VALUE_2318: verificatievergadering en zitting wijziging
        saneringsplan en beëindiging op [datum handeling] om [tijdstip]
        neerlegging slotuitdelingslijst vanaf [datum variabel]
        verification meeting and hearing on adjustment of restructuring
        plan and termination on [date] at [time] deposition of
        distribution list from [date]
    :cvar VALUE_2319: akkoordbehandeling op [datum handeling] om
        [tijdstip] hearing on agreement on [date] at [time]
    :cvar VALUE_2320: behandeling wijziging saneringsplan op [datum
        handeling] om [tijdstip] hearing on restructuring plan on [date]
        at [time]
    :cvar VALUE_2321: beëindigingszitting op [datum handeling] om
        [tijdstip] hearing on termination on [date] at [time]
    :cvar VALUE_2322: beëindigingszitting en wijziging saneringsplan op
        [datum handeling] om [tijdstip] hearing on termination and
        adjustment of restructuring plan on [date] at [time]
    :cvar VALUE_2323: beëindigingszitting op [datum handeling] om
        [tijdstip]  neerlegging slotuitdelingslijst vanaf [datum
        variabel] hearing on termination on [date] at [time]  deposition
        of final distribution list from [date]
    :cvar VALUE_2324: beëindigingszitting en wijziging saneringsplan op
        [datum handeling] om [tijdstip]  neerlegging slotuitdelingslijst
        vanaf [datum variabel] hearing on termination and adjustment of
        restructuring plan on [date] at [time]  deposition of  final
        distribution list from [date]
    :cvar VALUE_2325: vergadering van schuldeisers op [datum handeling]
        om [tijdstip] meeting of creditors on [date] at [time]
    :cvar VALUE_3305: behandeling verlenging termijn surseance op [datum
        handeling] om [tijdstip] hearing on extension of moratorium term
        on [date] at [time]
    :cvar VALUE_3306: crediteurenvergadering met akkoordbehandeling op
        [datum handeling] om [tijdstip] meeting of creditors with
        hearing on agreement on [date] at [time]
    :cvar VALUE_1312: neerlegging tussentijdse uitdelingslijst vanaf
        [datum variabel] deposition of interim distribution list from
        [date]
    :cvar VALUE_1313: neerlegging slotuitdelingslijst vanaf [datum
        variabel] deposition of final distribution list from [date]
    :cvar VALUE_1314: neerlegging slotuitdelingslijst vanaf [datum
        variabel] deposition of final distribution list from [date]
    :cvar VALUE_1315: vereenvoudigde afwikkeling van het faillissement
        en neerlegging slotuitdelingslijst vanaf [datum variabel]
        simplified bankruptcy proceedings and deposition of final
        distribution list from [date]
    :cvar VALUE_2326: neerlegging tussentijdse uitdelingslijst vanaf
        [datum variabel] deposition of interim distribution list from
        [date]
    :cvar VALUE_2327: neerlegging slotuitdelingslijst vanaf [datum
        variabel] deposition of final distribution list from [date]
    :cvar VALUE_1316: opheffing faillissement wegens gebrek aan baten op
        [datum handeling] removal from bankruptcy due to a lack of
        assets on [date]
    :cvar VALUE_1317: einde faillissement door verbindende
        uitdelingslijst op [datum handeling] termination of bankruptcy
        by binding distribution list on [date]
    :cvar VALUE_1318: einde faillissement door goedkeuring akkoord op
        [datum handeling] termination of bankruptcy by approval of
        agreement  on [date]
    :cvar VALUE_1319: einde faillissement door verbindende
        uitdelingslijst na verzet op [datum handeling] termination of
        bankruptcy by binding distribution list after opposition on
        [date]
    :cvar VALUE_1320: vernietiging faillissement na verzet op [datum
        handeling] nullification of bankruptcy after opposition on
        [date]
    :cvar VALUE_2337: vernietiging faillissement na verzet met herleving
        schuldsanering op [datum] nullification of bankruptcy after
        opposition with resurgence of debt restructuring on [date]
    :cvar VALUE_2328: einde schuldsanering omdat alle vorderingen zijn
        voldaan op [datum handeling] termination of debt restructuring
        because all debts are paid on [date]
    :cvar VALUE_2329: einde schuldsanering door hervatting betalingen op
        [datum handeling] termination of debt restructuring because of
        resumption of payments on [date]
    :cvar VALUE_2330: einde schuldsanering door goedkeuring akkoord op
        [datum handeling] termination of debt restructuring because of
        approval of agreement on [date]
    :cvar VALUE_2331: einde schuldsanering met uitdeling en met schone
        lei op [datum handeling] termination of debt restructuring with
        distribution and clean slate on [date]
    :cvar VALUE_2332: einde schuldsanering zonder uitdeling en met
        schone lei op [datum handeling] termination of debt
        restructuring without distribution, with clean slate on [date]
    :cvar VALUE_2333: einde schuldsanering met uitdeling en zonder
        schone lei op [datum handeling] termination of debt
        restructuring with distribution, without clean slate on [date]
    :cvar VALUE_2334: einde schuldsanering zonder uitdeling en zonder
        schone lei op [datum handeling] termination of debt
        restructuring without distribution, without clean slate on
        [date]
    :cvar VALUE_2335: einde schuldsanering door afwijzing definitieve
        schuldsanering op [datum handeling] termination of debt
        restructuring by rejection of final debt restructuring on [date]
    :cvar VALUE_3307: einde surseance op [datum handeling] termination
        of moratorium on [date]
    :cvar VALUE_3308: einde surseance wegens verlopen van de termijn op
        [datum handeling] termination of moratorium because of
        expiration of term on [date]
    :cvar VALUE_3309: einde surseance door goedkeuring akkoord op [datum
        handeling] termination of moratorium by approval of agreement on
        [date]
    :cvar VALUE_1322: indiening verzoek tot rehabilitatie door mr.
        [naam, adres, woonplaats procureur] filing of discharge request
        by mr. [name, address of solicitor]
    :cvar VALUE_2336: ontneming schone lei in schuldsanering op [datum
        handeling] deprivation of clean slate in debt restructuring on
        [date]
    :cvar VALUE_1324: einde faillissement door voldoen van alle schulden
        op [datum handeling] termination of bankruptcy because all debts
        are paid on [date]
    :cvar VALUE_1325: pro forma verificatievergadering pro forma
        verification meeting
    :cvar VALUE_1326: pro forma verificatievergadering en
        akkoordbehandeling pro forma verification meeting and hearing on
        agreement
    :cvar VALUE_2338: pro forma uitspraak schuldsanering en
        verificatievergadering pro forma admission to debt restructuring
        and verification meeting
    :cvar VALUE_2339: pro forma uitspraak schuldsanering en
        verificatievergadering met akkoordbehandeling pro forma
        admission to debt restructuring and verification meeting with
        hearing on agreement
    :cvar VALUE_2340: pro forma verificatievergadering pro forma
        verification meeting
    :cvar VALUE_2341: pro forma verificatievergadering en
        akkoordbehandeling pro forma verification meeting and hearing on
        agreement
    :cvar VALUE_2342: pro forma verificatievergadering, saneringsplan en
        akkoordbehandeling pro forma verification meeting, restructuring
        plan and hearing on agreemeent
    :cvar VALUE_2343: pro forma verificatievergadering en zitting
        wijziging saneringsplan pro forma verification meeting and
        hearing on adjustment of restructuring plan
    :cvar VALUE_2344: pro forma verificatievergadering en zitting
        beëindiging pro forma verification meeting, hearing on
        termination
    :cvar VALUE_2345: pro forma verificatievergadering en zitting
        beëindiging en neerlegging slotuitdelingslijst pro forma
        verification meeting, hearing on termination and deposition of
        distribution list
    :cvar VALUE_2346: pro forma verificatievergadering en zitting
        wijziging saneringsplan en beëindiging pro forma verification
        meeting and hearing on adjustment of restructuring plan and
        termination
    :cvar VALUE_2347: pro forma verificatievergadering en zitting
        wijziging saneringsplan en beëindiging en neerlegging
        slotuitdelingsl. vanaf pro forma verification meeting and
        hearing on adjustment of restructuring plan and termination and
        deposition of distribution list from
    :cvar VALUE_2348: rekening en verantwoording afgelegd rendered and
        accounted
    :cvar VALUE_1328: vervanging rechtercommissaris replacement
        supervisory judge
    :cvar VALUE_2349: vervanging rechtercommissaris replacement
        supervisory judge
    :cvar VALUE_3311: vervanging rechtercommissaris replacement
        supervisory judge
    :cvar VALUE_1330: aanvullende postblokkade additional mail blockade
    :cvar VALUE_1331: adreswijziging change of address
    :cvar VALUE_1332: tussentijdse intrekking postblokkade interim
        abrogation mail blockade
    :cvar VALUE_2351: aanvullende postblokkade additional mail blockade
    :cvar VALUE_2352: adreswijziging change of address
    :cvar VALUE_2353: tussentijdse intrekking postblokkade interim
        abrogation mail blockade
    :cvar VALUE_3313: Beëindiging door omzetting in faillissement op
        Termination of suspension of payments by conversion into
        bankruptcy on
    :cvar VALUE_1334: Faillissement overgedragen aan rechtbank:
        [rechtbank] op [datum] Bankruptcy transferred to court: [court]
        on [date]
    :cvar VALUE_1333: Faillissement omgezet in SSR op Bankruptcy
        converted into debt restructuring on
    :cvar VALUE_1335: Overig Other
    :cvar VALUE_2355: Schuldsanering overgedragen aan rechtbank:
        [rechtbank] op [datum] Debt restructuring transferred to court:
        [court] on [date]
    :cvar VALUE_2354: Tussentijdse beëindiging SSR met
        faillietverklaring op Premature termination of debt
        restructuring by declaration of bankruptcy on
    :cvar VALUE_3314: Surseance overgedragen aan rechtbank: [rechtbank]
        op [datum] Suspension of payments transferred to court: [court]
        on [date]
    :cvar VALUE_1336: Faillissement onterecht ingevoerd op [datum]
        Bankruptcy wrongly entered on [date]
    :cvar VALUE_2356: Schuldsanering onterecht ingevoerd op [datum] Debt
        restructuring wrongly entered on [date]
    :cvar VALUE_3315: Surseance onterecht ingevoerd op [datum]
        Suspension of payments wrongly entered on [date]
    :cvar VALUE_1329: Faillissement overgedragen van rechtbank:
        [rechtbank]. Uitgesproken op [datum] Bankruptcy transferred from
        court: [court]. Pronounced on [date]
    :cvar VALUE_2350: Schuldsanering overgedragen van rechtbank:
        [rechtbank]. Uitgesproken op [datum] Debt restructuring
        transferred from court: [court]. Pronounced on [date]
    :cvar VALUE_3316: Surseance overgedragen van rechtbank: [rechtbank].
        Uitgesproken op [datum] Suspension of payments transferred from
        court: [court]. Pronounced on [date]
    """

    VALUE_1200 = "1200"
    VALUE_1201 = "1201"
    VALUE_1202 = "1202"
    VALUE_2200 = "2200"
    VALUE_2201 = "2201"
    VALUE_2202 = "2202"
    VALUE_3200 = "3200"
    VALUE_3201 = "3201"
    VALUE_3202 = "3202"
    VALUE_1100 = "1100"
    VALUE_1101 = "1101"
    VALUE_1102 = "1102"
    VALUE_2100 = "2100"
    VALUE_2101 = "2101"
    VALUE_2102 = "2102"
    VALUE_3100 = "3100"
    VALUE_3101 = "3101"
    VALUE_3102 = "3102"
    VALUE_3310 = "3310"
    VALUE_1323 = "1323"
    VALUE_2300 = "2300"
    VALUE_1300 = "1300"
    VALUE_1301 = "1301"
    VALUE_1302 = "1302"
    VALUE_1303 = "1303"
    VALUE_1304 = "1304"
    VALUE_1305 = "1305"
    VALUE_1306 = "1306"
    VALUE_2301 = "2301"
    VALUE_2302 = "2302"
    VALUE_2303 = "2303"
    VALUE_2304 = "2304"
    VALUE_2305 = "2305"
    VALUE_2306 = "2306"
    VALUE_2307 = "2307"
    VALUE_2308 = "2308"
    VALUE_3300 = "3300"
    VALUE_3301 = "3301"
    VALUE_3302 = "3302"
    VALUE_3303 = "3303"
    VALUE_1307 = "1307"
    VALUE_2309 = "2309"
    VALUE_3304 = "3304"
    VALUE_1308 = "1308"
    VALUE_1309 = "1309"
    VALUE_1310 = "1310"
    VALUE_1311 = "1311"
    VALUE_2310 = "2310"
    VALUE_2311 = "2311"
    VALUE_2312 = "2312"
    VALUE_2313 = "2313"
    VALUE_2314 = "2314"
    VALUE_2315 = "2315"
    VALUE_2316 = "2316"
    VALUE_2317 = "2317"
    VALUE_2318 = "2318"
    VALUE_2319 = "2319"
    VALUE_2320 = "2320"
    VALUE_2321 = "2321"
    VALUE_2322 = "2322"
    VALUE_2323 = "2323"
    VALUE_2324 = "2324"
    VALUE_2325 = "2325"
    VALUE_3305 = "3305"
    VALUE_3306 = "3306"
    VALUE_1312 = "1312"
    VALUE_1313 = "1313"
    VALUE_1314 = "1314"
    VALUE_1315 = "1315"
    VALUE_2326 = "2326"
    VALUE_2327 = "2327"
    VALUE_1316 = "1316"
    VALUE_1317 = "1317"
    VALUE_1318 = "1318"
    VALUE_1319 = "1319"
    VALUE_1320 = "1320"
    VALUE_2337 = "2337"
    VALUE_2328 = "2328"
    VALUE_2329 = "2329"
    VALUE_2330 = "2330"
    VALUE_2331 = "2331"
    VALUE_2332 = "2332"
    VALUE_2333 = "2333"
    VALUE_2334 = "2334"
    VALUE_2335 = "2335"
    VALUE_3307 = "3307"
    VALUE_3308 = "3308"
    VALUE_3309 = "3309"
    VALUE_1322 = "1322"
    VALUE_2336 = "2336"
    VALUE_1324 = "1324"
    VALUE_1325 = "1325"
    VALUE_1326 = "1326"
    VALUE_2338 = "2338"
    VALUE_2339 = "2339"
    VALUE_2340 = "2340"
    VALUE_2341 = "2341"
    VALUE_2342 = "2342"
    VALUE_2343 = "2343"
    VALUE_2344 = "2344"
    VALUE_2345 = "2345"
    VALUE_2346 = "2346"
    VALUE_2347 = "2347"
    VALUE_2348 = "2348"
    VALUE_1328 = "1328"
    VALUE_2349 = "2349"
    VALUE_3311 = "3311"
    VALUE_1330 = "1330"
    VALUE_1331 = "1331"
    VALUE_1332 = "1332"
    VALUE_2351 = "2351"
    VALUE_2352 = "2352"
    VALUE_2353 = "2353"
    VALUE_3313 = "3313"
    VALUE_1334 = "1334"
    VALUE_1333 = "1333"
    VALUE_1335 = "1335"
    VALUE_2355 = "2355"
    VALUE_2354 = "2354"
    VALUE_3314 = "3314"
    VALUE_1336 = "1336"
    VALUE_2356 = "2356"
    VALUE_3315 = "3315"
    VALUE_1329 = "1329"
    VALUE_2350 = "2350"
    VALUE_3316 = "3316"


@dataclass
class InspubZittingslocatie:
    """
    Zittingslocatie location of hearings.
    """

    class Meta:
        name = "inspubZittingslocatie"

    straat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "max_length": 35,
        },
    )
    huisnummer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "max_length": 20,
        },
    )
    huisnummer_toevoeging: Optional[str] = field(
        default=None,
        metadata={
            "name": "huisnummerToevoeging",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 10,
        },
    )
    plaats: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "max_length": 40,
        },
    )


class Rechtspersoonlijkheid(Enum):
    """
    Legal personality.

    :cvar NATUURLIJK_PERSOON: natural person
    :cvar RECHTSPERSOON: legal person
    """

    NATUURLIJK_PERSOON = "natuurlijk persoon"
    RECHTSPERSOON = "rechtspersoon"


@dataclass
class VerslagBeperkt:
    class Meta:
        name = "verslagBeperkt"

    publicatiedatum_verslag: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publicatiedatumVerslag",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
        },
    )
    kenmerk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
        },
    )
    titel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
        },
    )
    eindverslag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "pattern": r"true|false",
        },
    )


@dataclass
class InspubAdresHandelsnaamElem:
    class Meta:
        name = "inspubAdresHandelsnaamElem"

    adres_type: Optional[InspubAdresType] = field(
        default=None,
        metadata={
            "name": "adresType",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
        },
    )
    datum_begin: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "datumBegin",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
        },
    )
    straat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "max_length": 35,
        },
    )
    huisnummer: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
        },
    )
    huisnummer_toevoeging1: Optional[str] = field(
        default=None,
        metadata={
            "name": "huisnummerToevoeging1",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 10,
        },
    )
    huisnummer_toevoeging2: Optional[str] = field(
        default=None,
        metadata={
            "name": "huisnummerToevoeging2",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 10,
        },
    )
    postcode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "length": 6,
            "pattern": r"[1-9][0-9]{3}[A-Z]{2}",
        },
    )
    plaats: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "max_length": 40,
        },
    )


@dataclass
class InspubCbvElem:
    class Meta:
        name = "inspubCbvElem"

    datum_begin: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "datumBegin",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
        },
    )
    datum_eind: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "datumEind",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
        },
    )
    titulatuur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 10,
        },
    )
    voorletters: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 20,
        },
    )
    voorvoegsel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 20,
        },
    )
    achternaam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "max_length": 200,
        },
    )
    cb: Optional[InspubCbvCb] = field(
        default=None,
        metadata={
            "name": "CB",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
        },
    )
    adres: Optional[InspubAdresCbelem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
        },
    )


@dataclass
class InspubPersoonWebsite:
    class Meta:
        name = "inspubPersoonWebsite"

    rechtspersoonlijkheid: Optional[Rechtspersoonlijkheid] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
        },
    )
    voornaam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 100,
        },
    )
    voorletters: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 20,
        },
    )
    voorvoegsel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 20,
        },
    )
    achternaam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 200,
        },
    )
    geboortedatum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
        },
    )
    geboorteplaats: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 40,
        },
    )
    geboorteland: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 50,
        },
    )
    overlijdensdatum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
        },
    )
    kv_knummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "KvKNummer",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "pattern": r"\d{5,8}",
        },
    )
    kv_kplaats: Optional[str] = field(
        default=None,
        metadata={
            "name": "KvKPlaats",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 40,
            "pattern": r"\D*",
        },
    )


@dataclass
class InspubPublicatiegeschiedenis:
    """
    History of publications.
    """

    class Meta:
        name = "inspubPublicatiegeschiedenis"

    publicatie: List["InspubPublicatiegeschiedenis.Publicatie"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "min_occurs": 1,
        },
    )
    instroom_legacy: Optional[str] = field(
        default=None,
        metadata={
            "name": "instroomLegacy",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "pattern": r"true|false",
        },
    )

    @dataclass
    class Publicatie:
        publicatie_datum: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "publicatieDatum",
                "type": "Element",
                "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
                "required": True,
            },
        )
        publicatie_kenmerk: Optional[str] = field(
            default=None,
            metadata={
                "name": "publicatieKenmerk",
                "type": "Element",
                "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
                "required": True,
                "pattern": r"([0-9]{2}\.){0,1}[a-z]{3}\.[0-9]{2}\.[0-9]{1,4}\.[F|S|R]\.[0-9]{4}\.[0-9]{1,2}\.[0-9]{2}",  # noqa: E501
            },
        )
        publicatie_omschrijving: Optional[str] = field(
            default=None,
            metadata={
                "name": "publicatieOmschrijving",
                "type": "Element",
                "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
                "required": True,
            },
        )
        publicatie_soort_code: Optional[InspubPublicatiesoortCode] = field(
            default=None,
            metadata={
                "name": "publicatieSoortCode",
                "type": "Element",
                "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
                "required": True,
            },
        )
        zittingslocatie: Optional[InspubZittingslocatie] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            },
        )
        publicerende_instantie_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "publicerendeInstantieCode",
                "type": "Element",
                "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
                "required": True,
            },
        )
        uiterstedatumindieningvorderingen: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            },
        )


@dataclass
class InspubCbvers:
    class Meta:
        name = "inspubCbvers"

    cbv: List[InspubCbvElem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "min_occurs": 1,
        },
    )


@dataclass
class InspubHandelendOnderDeNaamElem:
    class Meta:
        name = "inspubHandelendOnderDeNaamElem"

    handelsnaam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "required": True,
            "max_length": 200,
        },
    )
    kv_knummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "KvKNummer",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "pattern": r"\d{5,8}",
        },
    )
    kv_kplaats: Optional[str] = field(
        default=None,
        metadata={
            "name": "KvKPlaats",
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
            "max_length": 40,
            "pattern": r"\D*",
        },
    )
    handelsadressen: Optional["InspubHandelendOnderDeNaamElem.Handelsadressen"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
        },
    )

    @dataclass
    class Handelsadressen:
        handelsadres: List[InspubAdresHandelsnaamElem] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.rechtspraak.nl/namespaces/inspubber01",
                "min_occurs": 1,
            },
        )


@dataclass
class InspubWebserviceInsolvente:
    """
    insolventie insolvency.
    """

    class Meta:
        name = "inspubWebserviceInsolvente"
        namespace = "http://www.rechtspraak.nl/namespaces/inspubber01"

    insolvente: Optional["InspubWebserviceInsolvente.Insolvente"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exceptie: Optional["InspubWebserviceInsolvente.Exceptie"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Insolvente:
        """
        :ivar ssr_nummer:
        :ivar pre_hgkinsolventie_nummer:
        :ivar insolventienummer:
        :ivar behandelende_instantie_code:
        :ivar behandelende_instantie_naam:
        :ivar behandelende_vestiging_code:
        :ivar behandelende_vestiging_naam:
        :ivar is_pre_hgkgepubliceerd:
        :ivar persoon:
        :ivar rc:
        :ivar rc2:
        :ivar vorige_rc: Vorige rechter-commissaris Former supervisory
            judge
        :ivar vorig_insolventienummer:
        :ivar adressen:
        :ivar handelend_onder_de_namen:
        :ivar cbvers:
        :ivar publicatiegeschiedenis:
        :ivar beschikbare_verslagen:
        :ivar einde_vindbaarheid:
        """

        ssr_nummer: Optional[str] = field(
            default=None,
            metadata={
                "name": "ssrNummer",
                "type": "Element",
                "pattern": r"[A-Za-z]{3}\d{10}",
            },
        )
        pre_hgkinsolventie_nummer: Optional[str] = field(
            default=None,
            metadata={
                "name": "preHGKInsolventieNummer",
                "type": "Element",
                "pattern": r"[F|S|R]\.\d{2}/\d{1,4}",
            },
        )
        insolventienummer: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "pattern": r"[F|S|R]\.(\d{2}/){0,1}\d{2}/\d{1,4}",
            },
        )
        behandelende_instantie_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "behandelendeInstantieCode",
                "type": "Element",
                "required": True,
            },
        )
        behandelende_instantie_naam: Optional[str] = field(
            default=None,
            metadata={
                "name": "behandelendeInstantieNaam",
                "type": "Element",
                "required": True,
            },
        )
        behandelende_vestiging_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "behandelendeVestigingCode",
                "type": "Element",
                "required": True,
                "length": 4,
            },
        )
        behandelende_vestiging_naam: Optional[str] = field(
            default=None,
            metadata={
                "name": "behandelendeVestigingNaam",
                "type": "Element",
                "required": True,
                "max_length": 24,
            },
        )
        is_pre_hgkgepubliceerd: Optional[str] = field(
            default=None,
            metadata={
                "name": "isPreHGKGepubliceerd",
                "type": "Element",
                "required": True,
                "pattern": r"true|false",
            },
        )
        persoon: Optional[InspubPersoonWebsite] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        rc: Optional[str] = field(
            default=None,
            metadata={
                "name": "RC",
                "type": "Element",
                "max_length": 200,
            },
        )
        rc2: Optional[str] = field(
            default=None,
            metadata={
                "name": "RC2",
                "type": "Element",
                "max_length": 200,
            },
        )
        vorige_rc: Optional[str] = field(
            default=None,
            metadata={
                "name": "VorigeRC",
                "type": "Element",
                "max_length": 200,
            },
        )
        vorig_insolventienummer: Optional[str] = field(
            default=None,
            metadata={
                "name": "vorigInsolventienummer",
                "type": "Element",
                "pattern": r"[F|S|R]\.(\d{2}/){0,1}\d{2}/\d{1,4}",
            },
        )
        adressen: Optional["InspubWebserviceInsolvente.Insolvente.Adressen"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        handelend_onder_de_namen: Optional[
            "InspubWebserviceInsolvente.Insolvente.HandelendOnderDeNamen"
        ] = field(
            default=None,
            metadata={
                "name": "handelendOnderDeNamen",
                "type": "Element",
            },
        )
        cbvers: Optional[InspubCbvers] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        publicatiegeschiedenis: Optional[InspubPublicatiegeschiedenis] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        beschikbare_verslagen: Optional[
            "InspubWebserviceInsolvente.Insolvente.BeschikbareVerslagen"
        ] = field(
            default=None,
            metadata={
                "name": "beschikbareVerslagen",
                "type": "Element",
            },
        )
        einde_vindbaarheid: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "eindeVindbaarheid",
                "type": "Element",
            },
        )

        @dataclass
        class Adressen:
            geheim_adres: Optional[str] = field(
                default=None,
                metadata={
                    "name": "geheimAdres",
                    "type": "Element",
                    "required": True,
                    "pattern": r"true|false",
                },
            )
            adres: List["InspubWebserviceInsolvente.Insolvente.Adressen.Adres"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass
            class Adres(InspubAdresInsolvente):
                adres_type: Optional[InspubAdresType] = field(
                    default=None,
                    metadata={
                        "name": "adresType",
                        "type": "Element",
                        "required": True,
                    },
                )

        @dataclass
        class HandelendOnderDeNamen:
            handelend_onder_de_naam: List[
                "InspubWebserviceInsolvente.Insolvente.HandelendOnderDeNamen.HandelendOnderDeNaam"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "handelendOnderDeNaam",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass
            class HandelendOnderDeNaam(InspubHandelendOnderDeNaamElem):
                voorheen: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"true|false",
                    },
                )

        @dataclass
        class BeschikbareVerslagen:
            verslag: List[VerslagBeperkt] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
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
