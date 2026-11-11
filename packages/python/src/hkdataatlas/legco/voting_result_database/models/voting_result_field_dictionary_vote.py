from typing import Literal

VotingResultFieldDictionaryVote = Literal["Absent", "Abstain", "No", "Present", "Yes"]

VOTING_RESULT_FIELD_DICTIONARY_VOTE_VALUES: set[VotingResultFieldDictionaryVote] = {
    "Absent",
    "Abstain",
    "No",
    "Present",
    "Yes",
}


def check_voting_result_field_dictionary_vote(
    value: str,
) -> VotingResultFieldDictionaryVote:
    if value in VOTING_RESULT_FIELD_DICTIONARY_VOTE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VOTING_RESULT_FIELD_DICTIONARY_VOTE_VALUES!r}"
    )
