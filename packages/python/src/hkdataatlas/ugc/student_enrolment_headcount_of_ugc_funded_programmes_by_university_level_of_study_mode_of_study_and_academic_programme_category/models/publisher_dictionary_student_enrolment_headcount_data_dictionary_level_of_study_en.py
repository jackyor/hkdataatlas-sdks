from typing import Literal

PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyEN = Literal[
    "Research Postgraduate", "Sub-degree", "Taught Postgraduate", "Undergraduate"
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_LEVEL_OF_STUDY_EN_VALUES: set[
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyEN
] = {
    "Research Postgraduate",
    "Sub-degree",
    "Taught Postgraduate",
    "Undergraduate",
}


def check_publisher_dictionary_student_enrolment_headcount_data_dictionary_level_of_study_en(
    value: str,
) -> PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyEN:
    if (
        value
        in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_LEVEL_OF_STUDY_EN_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_LEVEL_OF_STUDY_EN_VALUES!r}"
    )
