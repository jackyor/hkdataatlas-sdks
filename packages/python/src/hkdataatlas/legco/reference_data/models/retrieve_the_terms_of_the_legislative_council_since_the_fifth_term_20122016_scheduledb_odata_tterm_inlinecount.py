from typing import Literal

RetrieveTheTermsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOdataTtermInlinecount = Literal[
    "allpages"
]

RETRIEVE_THE_TERMS_OF_THE_LEGISLATIVE_COUNCIL_SINCE_THE_FIFTH_TERM_20122016_SCHEDULEDB_ODATA_TTERM_INLINECOUNT_VALUES: set[
    RetrieveTheTermsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOdataTtermInlinecount
] = {
    "allpages",
}


def check_retrieve_the_terms_of_the_legislative_council_since_the_fifth_term_20122016_scheduledb_odata_tterm_inlinecount(
    value: str,
) -> RetrieveTheTermsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOdataTtermInlinecount:
    if (
        value
        in RETRIEVE_THE_TERMS_OF_THE_LEGISLATIVE_COUNCIL_SINCE_THE_FIFTH_TERM_20122016_SCHEDULEDB_ODATA_TTERM_INLINECOUNT_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_THE_TERMS_OF_THE_LEGISLATIVE_COUNCIL_SINCE_THE_FIFTH_TERM_20122016_SCHEDULEDB_ODATA_TTERM_INLINECOUNT_VALUES!r}"
    )
