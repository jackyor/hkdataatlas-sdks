from typing import Literal

VotingResultFieldDictionaryGcResultType2Type1 = Literal["Negatived", "Passed"]

VOTING_RESULT_FIELD_DICTIONARY_GC_RESULT_TYPE_2_TYPE_1_VALUES: set[
    VotingResultFieldDictionaryGcResultType2Type1
] = {
    "Negatived",
    "Passed",
}


def check_voting_result_field_dictionary_gc_result_type_2_type_1(
    value: str,
) -> VotingResultFieldDictionaryGcResultType2Type1:
    if value in VOTING_RESULT_FIELD_DICTIONARY_GC_RESULT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VOTING_RESULT_FIELD_DICTIONARY_GC_RESULT_TYPE_2_TYPE_1_VALUES!r}"
    )
