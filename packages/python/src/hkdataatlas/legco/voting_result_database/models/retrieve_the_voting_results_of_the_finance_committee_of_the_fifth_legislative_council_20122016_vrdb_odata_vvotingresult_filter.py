from typing import Literal

RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFilter = Literal[
    "type eq 'Finance Committee' and start_date ge datetime'2012-10-01' and start_date lt datetime'2016-10-01'"
]

RETRIEVE_THE_VOTING_RESULTS_OF_THE_FINANCE_COMMITTEE_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_VRDB_ODATA_VVOTINGRESULT_FILTER_VALUES: set[
    RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFilter
] = {
    "type eq 'Finance Committee' and start_date ge datetime'2012-10-01' and start_date lt datetime'2016-10-01'",
}


def check_retrieve_the_voting_results_of_the_finance_committee_of_the_fifth_legislative_council_20122016_vrdb_odata_vvotingresult_filter(
    value: str,
) -> RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFilter:
    if (
        value
        in RETRIEVE_THE_VOTING_RESULTS_OF_THE_FINANCE_COMMITTEE_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_VRDB_ODATA_VVOTINGRESULT_FILTER_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_THE_VOTING_RESULTS_OF_THE_FINANCE_COMMITTEE_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_VRDB_ODATA_VVOTINGRESULT_FILTER_VALUES!r}"
    )
