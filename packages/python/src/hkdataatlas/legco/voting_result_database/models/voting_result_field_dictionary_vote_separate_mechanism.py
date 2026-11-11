from typing import Literal

VotingResultFieldDictionaryVoteSeparateMechanism = Literal["No", "Yes"]

VOTING_RESULT_FIELD_DICTIONARY_VOTE_SEPARATE_MECHANISM_VALUES: set[
    VotingResultFieldDictionaryVoteSeparateMechanism
] = {
    "No",
    "Yes",
}


def check_voting_result_field_dictionary_vote_separate_mechanism(
    value: str,
) -> VotingResultFieldDictionaryVoteSeparateMechanism:
    if value in VOTING_RESULT_FIELD_DICTIONARY_VOTE_SEPARATE_MECHANISM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VOTING_RESULT_FIELD_DICTIONARY_VOTE_SEPARATE_MECHANISM_VALUES!r}"
    )
