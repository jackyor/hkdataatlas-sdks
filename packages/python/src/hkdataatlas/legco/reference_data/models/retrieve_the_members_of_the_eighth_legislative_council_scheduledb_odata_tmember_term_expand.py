from typing import Literal

RetrieveTheMembersOfTheEighthLegislativeCouncilScheduledbOdataTmemberTermExpand = (
    Literal["Tmember"]
)

RETRIEVE_THE_MEMBERS_OF_THE_EIGHTH_LEGISLATIVE_COUNCIL_SCHEDULEDB_ODATA_TMEMBER_TERM_EXPAND_VALUES: set[
    RetrieveTheMembersOfTheEighthLegislativeCouncilScheduledbOdataTmemberTermExpand
] = {
    "Tmember",
}


def check_retrieve_the_members_of_the_eighth_legislative_council_scheduledb_odata_tmember_term_expand(
    value: str,
) -> RetrieveTheMembersOfTheEighthLegislativeCouncilScheduledbOdataTmemberTermExpand:
    if (
        value
        in RETRIEVE_THE_MEMBERS_OF_THE_EIGHTH_LEGISLATIVE_COUNCIL_SCHEDULEDB_ODATA_TMEMBER_TERM_EXPAND_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_THE_MEMBERS_OF_THE_EIGHTH_LEGISLATIVE_COUNCIL_SCHEDULEDB_ODATA_TMEMBER_TERM_EXPAND_VALUES!r}"
    )
