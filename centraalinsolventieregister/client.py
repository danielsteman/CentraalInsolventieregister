import os
import uuid
from typing import Literal

from dotenv import load_dotenv
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element
from suds.wsse import Security, UsernameToken

from centraalinsolventieregister.rspublic_ws_insolvency_content_with_reports03 import (
    InspubWebserviceInsolvente,
)
from centraalinsolventieregister.rspublic_ws_insolvency_requests import (
    InstantieRechtbankCode,
    SearchByDatePubType,
)
from centraalinsolventieregister.rspublic_ws_insolvency_response_list01 import (
    PublicatieLijst,
)

load_dotenv()


WEBSERVICE_URL = "http://webservice.rechtspraak.nl/cir.asmx?wsdl"
NS_WSA = ("wsa", "http://schemas.xmlsoap.org/ws/2004/08/addressing")
MUST_UNDERSTAND = Attribute("SOAP-ENV:mustUnderstand", "true")


USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


PubType = Literal["Uitspraken faillissement"]


class CIRClient:
    def __init__(self) -> None:
        self.client = Client(WEBSERVICE_URL)
        self.set_security_options()
        self.set_headers()

    def set_security_options(self):
        sec = Security()
        token = UsernameToken(USERNAME, PASSWORD)
        token.setnonce()
        sec.tokens.append(token)
        self.client.set_options(wsse=sec)

    def set_headers(self):
        headers = []
        headers.append(
            Element("Element").addPrefix(
                p="SOAP-ENC", u="http://www.w3.org/2003/05/soap-encoding"
            )
        )
        addr = Element("Address", ns=NS_WSA).setText(
            "http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous"
        )
        headers.append(
            Element("ReplyTo", ns=NS_WSA).insert(addr).append(MUST_UNDERSTAND)
        )
        headers.append(
            Element("To", ns=NS_WSA).setText(WEBSERVICE_URL).append(MUST_UNDERSTAND)
        )
        headers.append(addr)
        headers.append(
            Element("MessageID", ns=NS_WSA).setText(
                "urn:uuid:%s" % self.generate_messageid()
            )
        )
        headers.append(Element("Action", ns=NS_WSA))
        self.client.set_options(soapheaders=headers)

    @classmethod
    def generate_messageid(cls):
        return str(uuid.uuid4())

    def ping(self):
        return self.client.service.Ping()

    def get_court_list(self):
        return

    def get_cases_by_date(
        self, date: str, court: InstantieRechtbankCode, pub_type: SearchByDatePubType
    ) -> PublicatieLijst:
        res = self.client.service.searchByDate(date, court.value, pub_type.value)
        res = res.publicatieLijst
        try:
            exception = res.exceptie.value
            return PublicatieLijst(exceptie=exception)
        except AttributeError:
            exception = None

        publication_feature = res.publicatieKenmerk
        extraction_date = res._extractiedatum

        publication_list = PublicatieLijst(
            exceptie=exception,
            publicatie_kenmerk=publication_feature,
            extractiedatum=extraction_date,
        )
        return publication_list

    def get_case(self, case_id: str) -> InspubWebserviceInsolvente:
        res = self.client.service.getCase(case_id)
        res = res.inspubWebserviceInsolvente

        try:
            exception = res.exceptie.value
            return InspubWebserviceInsolvente(exceptie=exception)
        except AttributeError:
            exception = None

        return InspubWebserviceInsolvente(insolvente=res.insolvente)

    def get_case_kvk(self, case_id: str) -> int | None:
        case = self.get_case(case_id)
        case = case.insolvente

        try:
            return case.insolvente.handelendOnderDeNamen.handelendOnderDeNaam
        except AttributeError as e:
            print(e)
            return None
