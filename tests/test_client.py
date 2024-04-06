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
