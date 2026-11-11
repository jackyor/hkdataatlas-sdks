from typing import Literal

PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyEN = Literal[
    "Full-time", "Part-time"
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_MODE_OF_STUDY_EN_VALUES: set[
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyEN
] = {
    "Full-time",
    "Part-time",
}


def check_publisher_dictionary_student_enrolment_headcount_data_dictionary_mode_of_study_en(
    value: str,
) -> PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyEN:
    if (
        value
        in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_MODE_OF_STUDY_EN_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_MODE_OF_STUDY_EN_VALUES!r}"
    )
