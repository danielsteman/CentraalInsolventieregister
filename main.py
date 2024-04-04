from suds.client import Client
from suds.wsse import Security, UsernameToken
import configparser
from suds.sax.element import Element
from suds.sax.attribute import Attribute
import string
import random


def generate_messageid():
    fmt = "xxxxxxxx-xxxxx"
    resp = ""

    for c in fmt:
        if c == "-":
            resp += c
        else:
            resp += string.hexdigits[random.randrange(16)]

    return resp


WEBSERVICE_URL = "http://webservice.rechtspraak.nl/cir.asmx?wsdl"
NS_WSA = ("wsa", "http://schemas.xmlsoap.org/ws/2004/08/addressing")
MUST_UNDERSTAND = Attribute("SOAP-ENV:mustUnderstand", "true")

Config = configparser.ConfigParser()
Config.read("credentials.ini")

USERNAME = Config.get("Login", "Username")
PASSWORD = Config.get("Login", "Password")

client = Client(WEBSERVICE_URL)

sec = Security()
token = UsernameToken(USERNAME, PASSWORD)
token.setnonce()
sec.tokens.append(token)
client.set_options(wsse=sec)

headers = []
addr = Element("Address", ns=NS_WSA).setText(
    "http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous"
)
headers.append(
    Element("Element").addPrefix(
        p="SOAP-ENC", u="http://www.w3.org/2003/05/soap-encoding"
    )
)
headers.append(Element("ReplyTo", ns=NS_WSA).insert(addr).append(MUST_UNDERSTAND))
headers.append(Element("To", ns=NS_WSA).setText(WEBSERVICE_URL).append(MUST_UNDERSTAND))
headers.append(addr)
headers.append(
    Element("MessageID", ns=NS_WSA).setText("urn:uuid:%s" % generate_messageid())
)
action = "http://www.rechtspraak.nl/namespaces/cir01/Ping"
headers.append(Element("Action", ns=NS_WSA).setText(action))

client.set_options(soapheaders=headers)

ping_response = client.service.Ping()
search_by_date_response = client.service.searchByDate(
    "2024-04-01T00:00:00", "41", "Uitspraken faillissement"
)


# search_by_date_response = client.service
