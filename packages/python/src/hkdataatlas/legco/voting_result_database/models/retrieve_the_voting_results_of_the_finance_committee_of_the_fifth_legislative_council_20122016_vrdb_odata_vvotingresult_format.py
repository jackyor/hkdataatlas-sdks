from typing import Literal

RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFormat = Literal[
    "xml"
]

RETRIEVE_THE_VOTING_RESULTS_OF_THE_FINANCE_COMMITTEE_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_VRDB_ODATA_VVOTINGRESULT_FORMAT_VALUES: set[
    RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFormat
] = {
    "xml",
}


def check_retrieve_the_voting_results_of_the_finance_committee_of_the_fifth_legislative_council_20122016_vrdb_odata_vvotingresult_format(
    value: str,
) -> RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFormat:
    if (
        value
        in RETRIEVE_THE_VOTING_RESULTS_OF_THE_FINANCE_COMMITTEE_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_VRDB_ODATA_VVOTINGRESULT_FORMAT_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_THE_VOTING_RESULTS_OF_THE_FINANCE_COMMITTEE_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_VRDB_ODATA_VVOTINGRESULT_FORMAT_VALUES!r}"
    )
