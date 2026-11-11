from typing import Literal

PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyTC = Literal[
    "全日制", "兼讀制"
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_MODE_OF_STUDY_TC_VALUES: set[
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyTC
] = {
    "全日制",
    "兼讀制",
}


def check_publisher_dictionary_student_enrolment_headcount_data_dictionary_mode_of_study_tc(
    value: str,
) -> PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyTC:
    if (
        value
        in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_MODE_OF_STUDY_TC_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_MODE_OF_STUDY_TC_VALUES!r}"
    )
