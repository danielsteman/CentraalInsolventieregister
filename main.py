import os
import uuid

from dotenv import load_dotenv
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.element import Element
from suds.wsse import Security, UsernameToken

load_dotenv()


WEBSERVICE_URL = "http://webservice.rechtspraak.nl/cir.asmx?wsdl"
NS_WSA = ("wsa", "http://schemas.xmlsoap.org/ws/2004/08/addressing")
MUST_UNDERSTAND = Attribute("SOAP-ENV:mustUnderstand", "true")


USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


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


client = CIRClient()
res = client.ping()
print(res)
court_list = client.get_court_list()
print(court_list)


# client = Client(WEBSERVICE_URL)

# sec = Security()
# token = UsernameToken(USERNAME, PASSWORD)
# token.setnonce()
# sec.tokens.append(token)
# client.set_options(wsse=sec)

# headers = []
# addr = Element("Address", ns=NS_WSA).setText(
#     "http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous"
# )
# headers.append(
#     Element("Element").addPrefix(
#         p="SOAP-ENC", u="http://www.w3.org/2003/05/soap-encoding"
#     )
# )
# headers.append(Element("ReplyTo", ns=NS_WSA).insert(addr).append(MUST_UNDERSTAND))
# headers.append(Element("To", ns=NS_WSA).setText(WEBSERVICE_URL).append(
#   MUST_UNDERSTAND
# ))
# headers.append(addr)
# headers.append(
#     Element("MessageID", ns=NS_WSA).setText("urn:uuid:%s" % generate_messageid())
# )
# action = "http://www.rechtspraak.nl/namespaces/cir01/Ping"
# # headers.append(Element("Action", ns=NS_WSA).setText(action))
# headers.append(Element("Action", ns=NS_WSA))

# client.set_options(soapheaders=headers)

# ping_response = client.service.Ping()
# search_by_date_response = client.service.searchByDate(
#     "2024-04-01T00:00:00", "41", "Uitspraken faillissement"
# )
# case_id = "15.nho.24.94.F.1300.1.24"
# case_response = client.service.getCase(case_id)
# # print(client)
# print(case_response)
# # print(search_by_date_response)
# # search_by_date_response = client.service
