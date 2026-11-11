from typing import Literal

PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyEN = Literal[
    "Full-time", "Part-time"
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_MODE_OF_STUDY_EN_VALUES: set[
    PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyEN
] = {
    "Full-time",
    "Part-time",
}


def check_publisher_dictionary_student_enrolment_data_dictionary_mode_of_study_en(
    value: str,
) -> PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyEN:
    if (
        value
        in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_MODE_OF_STUDY_EN_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_MODE_OF_STUDY_EN_VALUES!r}"
    )
