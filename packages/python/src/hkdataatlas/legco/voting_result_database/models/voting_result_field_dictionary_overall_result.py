from typing import Literal

VotingResultFieldDictionaryOverallResult = Literal["Negatived", "Passed", "Tied"]

VOTING_RESULT_FIELD_DICTIONARY_OVERALL_RESULT_VALUES: set[
    VotingResultFieldDictionaryOverallResult
] = {
    "Negatived",
    "Passed",
    "Tied",
}


def check_voting_result_field_dictionary_overall_result(
    value: str,
) -> VotingResultFieldDictionaryOverallResult:
    if value in VOTING_RESULT_FIELD_DICTIONARY_OVERALL_RESULT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VOTING_RESULT_FIELD_DICTIONARY_OVERALL_RESULT_VALUES!r}"
    )
