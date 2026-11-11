from typing import Literal

RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFilter = Literal[
    "bill_gazette_date ge datetime'1997-07-01' and bill_gazette_date lt datetime'1998-07-01'",
    "bill_gazette_date ge datetime'1998-07-01' and bill_gazette_date lt datetime'2000-10-01'",
    "bill_gazette_date ge datetime'2000-10-01' and bill_gazette_date lt datetime'2004-10-01'",
    "bill_gazette_date ge datetime'2004-10-01' and bill_gazette_date lt datetime'2008-10-01'",
    "bill_gazette_date ge datetime'2008-10-01' and bill_gazette_date lt datetime'2012-10-01'",
    "bill_gazette_date ge datetime'2012-10-01' and bill_gazette_date lt datetime'2016-10-01'",
    "bill_gazette_date ge datetime'2016-10-01' and bill_gazette_date lt datetime'2022-01-01'",
    "bill_gazette_date ge datetime'2022-01-01' and bill_gazette_date lt datetime'2026-01-01'",
    "bill_gazette_date ge datetime'2026-01-01' and bill_gazette_date lt datetime'2030-01-01'",
    "bill_gazette_date lt datetime'1997-07-01'",
]

RETRIEVE_BILLS_GAZETTED_DURING_THE_PROVISIONAL_LEGISLATIVE_COUNCIL_19971998_BILLSDB_ODATA_VBILLS_FILTER_VALUES: set[
    RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFilter
] = {
    "bill_gazette_date ge datetime'1997-07-01' and bill_gazette_date lt datetime'1998-07-01'",
    "bill_gazette_date ge datetime'1998-07-01' and bill_gazette_date lt datetime'2000-10-01'",
    "bill_gazette_date ge datetime'2000-10-01' and bill_gazette_date lt datetime'2004-10-01'",
    "bill_gazette_date ge datetime'2004-10-01' and bill_gazette_date lt datetime'2008-10-01'",
    "bill_gazette_date ge datetime'2008-10-01' and bill_gazette_date lt datetime'2012-10-01'",
    "bill_gazette_date ge datetime'2012-10-01' and bill_gazette_date lt datetime'2016-10-01'",
    "bill_gazette_date ge datetime'2016-10-01' and bill_gazette_date lt datetime'2022-01-01'",
    "bill_gazette_date ge datetime'2022-01-01' and bill_gazette_date lt datetime'2026-01-01'",
    "bill_gazette_date ge datetime'2026-01-01' and bill_gazette_date lt datetime'2030-01-01'",
    "bill_gazette_date lt datetime'1997-07-01'",
}


def check_retrieve_bills_gazetted_during_the_provisional_legislative_council_19971998_billsdb_odata_vbills_filter(
    value: str,
) -> RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFilter:
    if (
        value
        in RETRIEVE_BILLS_GAZETTED_DURING_THE_PROVISIONAL_LEGISLATIVE_COUNCIL_19971998_BILLSDB_ODATA_VBILLS_FILTER_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_BILLS_GAZETTED_DURING_THE_PROVISIONAL_LEGISLATIVE_COUNCIL_19971998_BILLSDB_ODATA_VBILLS_FILTER_VALUES!r}"
    )
