from typing import Literal

RetrieveTheMembersOfTheEighthLegislativeCouncilScheduledbOdataTmemberTermFilter = (
    Literal["term_id eq 7"]
)

RETRIEVE_THE_MEMBERS_OF_THE_EIGHTH_LEGISLATIVE_COUNCIL_SCHEDULEDB_ODATA_TMEMBER_TERM_FILTER_VALUES: set[
    RetrieveTheMembersOfTheEighthLegislativeCouncilScheduledbOdataTmemberTermFilter
] = {
    "term_id eq 7",
}


def check_retrieve_the_members_of_the_eighth_legislative_council_scheduledb_odata_tmember_term_filter(
    value: str,
) -> RetrieveTheMembersOfTheEighthLegislativeCouncilScheduledbOdataTmemberTermFilter:
    if (
        value
        in RETRIEVE_THE_MEMBERS_OF_THE_EIGHTH_LEGISLATIVE_COUNCIL_SCHEDULEDB_ODATA_TMEMBER_TERM_FILTER_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_THE_MEMBERS_OF_THE_EIGHTH_LEGISLATIVE_COUNCIL_SCHEDULEDB_ODATA_TMEMBER_TERM_FILTER_VALUES!r}"
    )
