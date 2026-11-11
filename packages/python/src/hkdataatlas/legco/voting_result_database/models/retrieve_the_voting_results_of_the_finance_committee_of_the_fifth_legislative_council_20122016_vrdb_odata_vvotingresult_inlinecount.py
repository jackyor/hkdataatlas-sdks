from typing import Literal

RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultInlinecount = Literal[
    "allpages"
]

RETRIEVE_THE_VOTING_RESULTS_OF_THE_FINANCE_COMMITTEE_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_VRDB_ODATA_VVOTINGRESULT_INLINECOUNT_VALUES: set[
    RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultInlinecount
] = {
    "allpages",
}


def check_retrieve_the_voting_results_of_the_finance_committee_of_the_fifth_legislative_council_20122016_vrdb_odata_vvotingresult_inlinecount(
    value: str,
) -> RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultInlinecount:
    if (
        value
        in RETRIEVE_THE_VOTING_RESULTS_OF_THE_FINANCE_COMMITTEE_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_VRDB_ODATA_VVOTINGRESULT_INLINECOUNT_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_THE_VOTING_RESULTS_OF_THE_FINANCE_COMMITTEE_OF_THE_FIFTH_LEGISLATIVE_COUNCIL_20122016_VRDB_ODATA_VVOTINGRESULT_INLINECOUNT_VALUES!r}"
    )
