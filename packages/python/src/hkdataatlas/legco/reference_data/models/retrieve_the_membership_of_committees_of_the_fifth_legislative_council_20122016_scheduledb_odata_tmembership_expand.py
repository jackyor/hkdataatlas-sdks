from typing import Literal

RetrieveTheMembershipOfCommitteesOfTheFifthLegislativeCouncil20122016ScheduledbOdataTmembershipExpand = Literal[
    "Tcommittee"
]

RETRIEVE_THE_MEMBERSHIP_OF_COMMITTEES_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_SCHEDULEDB_ODATA_TMEMBERSHIP_EXPAND_VALUES: set[
    RetrieveTheMembershipOfCommitteesOfTheFifthLegislativeCouncil20122016ScheduledbOdataTmembershipExpand
] = {
    "Tcommittee",
}


def check_retrieve_the_membership_of_committees_of_the_fifth_legislative_council_20122016_scheduledb_odata_tmembership_expand(
    value: str,
) -> RetrieveTheMembershipOfCommitteesOfTheFifthLegislativeCouncil20122016ScheduledbOdataTmembershipExpand:
    if (
        value
        in RETRIEVE_THE_MEMBERSHIP_OF_COMMITTEES_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_SCHEDULEDB_ODATA_TMEMBERSHIP_EXPAND_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_THE_MEMBERSHIP_OF_COMMITTEES_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_SCHEDULEDB_ODATA_TMEMBERSHIP_EXPAND_VALUES!r}"
    )
