from typing import Literal

RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFormat = Literal[
    "xml"
]

RETRIEVE_THE_COMMITTEES_OF_THE_SIXTH_LEGISLATIVE_COUNCIL_20162021_SCHEDULEDB_ODATA_TCOMMITTEE_FORMAT_VALUES: set[
    RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFormat
] = {
    "xml",
}


def check_retrieve_the_committees_of_the_sixth_legislative_council_20162021_scheduledb_odata_tcommittee_format(
    value: str,
) -> RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFormat:
    if (
        value
        in RETRIEVE_THE_COMMITTEES_OF_THE_SIXTH_LEGISLATIVE_COUNCIL_20162021_SCHEDULEDB_ODATA_TCOMMITTEE_FORMAT_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_THE_COMMITTEES_OF_THE_SIXTH_LEGISLATIVE_COUNCIL_20162021_SCHEDULEDB_ODATA_TCOMMITTEE_FORMAT_VALUES!r}"
    )
