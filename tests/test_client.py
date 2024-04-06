from centraalinsolventieregister.client import CIRClient
from centraalinsolventieregister.rspublic_ws_insolvency_requests import (
    InstantieRechtbankCode,
    SearchByDatePubType,
)


def test_client_get_cases_by_date():
    client = CIRClient()
    res = client.get_cases_by_date(
        "2024-04-04T00:00:00",
        InstantieRechtbankCode.ROTTERDAM2,
        SearchByDatePubType.UITSPRAKEN_FAILLISSEMENT,
    )
    assert len(res.publicatie_kenmerk) > 0


def test_get_case():
    case_id = "10.rot.23.279.F.1313.1.24"
    client = CIRClient()
    res = client.get_case(case_id)
    assert res.insolvente


def test_get_kvk():
    case_id = "10.rot.23.279.F.1313.1.24"
    client = CIRClient()
    kvk = client.get_case_kvk(case_id)
    assert kvk > 0
