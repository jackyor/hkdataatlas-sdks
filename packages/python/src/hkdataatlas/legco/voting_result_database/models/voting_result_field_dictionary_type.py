from typing import Literal

VotingResultFieldDictionaryType = Literal[
    "Council Meeting",
    "Establishment",
    "Finance Committee",
    "House Committee",
    "Public Works Subcommittee",
]

VOTING_RESULT_FIELD_DICTIONARY_TYPE_VALUES: set[VotingResultFieldDictionaryType] = {
    "Council Meeting",
    "Establishment",
    "Finance Committee",
    "House Committee",
    "Public Works Subcommittee",
}


def check_voting_result_field_dictionary_type(
    value: str,
) -> VotingResultFieldDictionaryType:
    if value in VOTING_RESULT_FIELD_DICTIONARY_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VOTING_RESULT_FIELD_DICTIONARY_TYPE_VALUES!r}"
    )
