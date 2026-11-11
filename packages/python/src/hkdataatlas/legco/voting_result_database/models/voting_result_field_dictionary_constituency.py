from typing import Literal

VotingResultFieldDictionaryConstituency = Literal["Functional", "Geographical"]

VOTING_RESULT_FIELD_DICTIONARY_CONSTITUENCY_VALUES: set[
    VotingResultFieldDictionaryConstituency
] = {
    "Functional",
    "Geographical",
}


def check_voting_result_field_dictionary_constituency(
    value: str,
) -> VotingResultFieldDictionaryConstituency:
    if value in VOTING_RESULT_FIELD_DICTIONARY_CONSTITUENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VOTING_RESULT_FIELD_DICTIONARY_CONSTITUENCY_VALUES!r}"
    )
