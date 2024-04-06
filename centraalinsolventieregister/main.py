import os
import uuid
from typing import Literal

from dotenv import load_dotenv
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element
from suds.wsse import Security, UsernameToken

from centraalinsolventieregister.rspublic_ws_insolvency_requests import (
    InstantieRechtbankCode,
    SearchByDatePubType,
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
    ):
        """
        Params:
            date: "2024-04-01T00:00:00"
            court: "41"
            type: "Uitspraken faillissement"
        """
        res = self.client.service.searchByDate(date, court.value, pub_type.value)
        return res

    def get_case(self, case_id: str):
        """
        Params:
            case_id: "15.nho.24.94.F.1300.1.24"
        """
        res = self.client.service.getCase(case_id)
        return res


client = CIRClient()
res = client.get_cases_by_date(
    "2024-04-01T00:00:00",
    InstantieRechtbankCode.ROTTERDAM2,
    SearchByDatePubType.UITSPRAKEN_FAILLISSEMENT,
)
print(res)
# court_list = client.get_court_list()
# print(court_list)
