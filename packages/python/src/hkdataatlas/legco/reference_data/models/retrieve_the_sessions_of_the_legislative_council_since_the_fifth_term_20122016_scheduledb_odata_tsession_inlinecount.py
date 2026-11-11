from typing import Literal

RetrieveTheSessionsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOdataTsessionInlinecount = Literal[
    "allpages"
]

RETRIEVE_THE_SESSIONS_OF_THE_LEGISLATIVE_COUNCIL_SINCE_THE_FIFTH_TERM_20122016_SCHEDULEDB_ODATA_TSESSION_INLINECOUNT_VALUES: set[
    RetrieveTheSessionsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOdataTsessionInlinecount
] = {
    "allpages",
}


def check_retrieve_the_sessions_of_the_legislative_council_since_the_fifth_term_20122016_scheduledb_odata_tsession_inlinecount(
    value: str,
) -> RetrieveTheSessionsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOdataTsessionInlinecount:
    if (
        value
        in RETRIEVE_THE_SESSIONS_OF_THE_LEGISLATIVE_COUNCIL_SINCE_THE_FIFTH_TERM_20122016_SCHEDULEDB_ODATA_TSESSION_INLINECOUNT_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_THE_SESSIONS_OF_THE_LEGISLATIVE_COUNCIL_SINCE_THE_FIFTH_TERM_20122016_SCHEDULEDB_ODATA_TSESSION_INLINECOUNT_VALUES!r}"
    )
