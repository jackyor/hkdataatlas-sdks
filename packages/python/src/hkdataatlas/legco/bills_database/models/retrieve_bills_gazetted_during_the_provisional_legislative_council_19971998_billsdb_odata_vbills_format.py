from typing import Literal

RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFormat = Literal[
    "json", "xml"
]

RETRIEVE_BILLS_GAZETTED_DURING_THE_PROVISIONAL_LEGISLATIVE_COUNCIL_19971998_BILLSDB_ODATA_VBILLS_FORMAT_VALUES: set[
    RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFormat
] = {
    "json",
    "xml",
}


def check_retrieve_bills_gazetted_during_the_provisional_legislative_council_19971998_billsdb_odata_vbills_format(
    value: str,
) -> RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFormat:
    if (
        value
        in RETRIEVE_BILLS_GAZETTED_DURING_THE_PROVISIONAL_LEGISLATIVE_COUNCIL_19971998_BILLSDB_ODATA_VBILLS_FORMAT_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_BILLS_GAZETTED_DURING_THE_PROVISIONAL_LEGISLATIVE_COUNCIL_19971998_BILLSDB_ODATA_VBILLS_FORMAT_VALUES!r}"
    )
