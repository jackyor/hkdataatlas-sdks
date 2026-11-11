from typing import Literal

RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsInlinecount = Literal[
    "allpages"
]

RETRIEVE_BILLS_GAZETTED_DURING_THE_PROVISIONAL_LEGISLATIVE_COUNCIL_19971998_BILLSDB_ODATA_VBILLS_INLINECOUNT_VALUES: set[
    RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsInlinecount
] = {
    "allpages",
}


def check_retrieve_bills_gazetted_during_the_provisional_legislative_council_19971998_billsdb_odata_vbills_inlinecount(
    value: str,
) -> RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsInlinecount:
    if (
        value
        in RETRIEVE_BILLS_GAZETTED_DURING_THE_PROVISIONAL_LEGISLATIVE_COUNCIL_19971998_BILLSDB_ODATA_VBILLS_INLINECOUNT_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_BILLS_GAZETTED_DURING_THE_PROVISIONAL_LEGISLATIVE_COUNCIL_19971998_BILLSDB_ODATA_VBILLS_INLINECOUNT_VALUES!r}"
    )
