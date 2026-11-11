from typing import Literal

VotingResultFieldDictionaryMoverType = Literal["Member", "Public Officer"]

VOTING_RESULT_FIELD_DICTIONARY_MOVER_TYPE_VALUES: set[
    VotingResultFieldDictionaryMoverType
] = {
    "Member",
    "Public Officer",
}


def check_voting_result_field_dictionary_mover_type(
    value: str,
) -> VotingResultFieldDictionaryMoverType:
    if value in VOTING_RESULT_FIELD_DICTIONARY_MOVER_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VOTING_RESULT_FIELD_DICTIONARY_MOVER_TYPE_VALUES!r}"
    )
