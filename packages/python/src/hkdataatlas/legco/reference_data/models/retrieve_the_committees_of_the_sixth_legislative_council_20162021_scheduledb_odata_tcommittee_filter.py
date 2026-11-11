from typing import Literal

RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFilter = Literal[
    "term_id eq 5"
]

RETRIEVE_THE_COMMITTEES_OF_THE_SIXTH_LEGISLATIVE_COUNCIL_20162021_SCHEDULEDB_ODATA_TCOMMITTEE_FILTER_VALUES: set[
    RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFilter
] = {
    "term_id eq 5",
}


def check_retrieve_the_committees_of_the_sixth_legislative_council_20162021_scheduledb_odata_tcommittee_filter(
    value: str,
) -> RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFilter:
    if (
        value
        in RETRIEVE_THE_COMMITTEES_OF_THE_SIXTH_LEGISLATIVE_COUNCIL_20162021_SCHEDULEDB_ODATA_TCOMMITTEE_FILTER_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_THE_COMMITTEES_OF_THE_SIXTH_LEGISLATIVE_COUNCIL_20162021_SCHEDULEDB_ODATA_TCOMMITTEE_FILTER_VALUES!r}"
    )
