from typing import Literal

PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyTC = Literal[
    "副學位課程", "學士學位課程", "研究院修課課程", "研究院研究課程"
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_LEVEL_OF_STUDY_TC_VALUES: set[
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyTC
] = {
    "副學位課程",
    "學士學位課程",
    "研究院修課課程",
    "研究院研究課程",
}


def check_publisher_dictionary_student_enrolment_headcount_data_dictionary_level_of_study_tc(
    value: str,
) -> PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyTC:
    if (
        value
        in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_LEVEL_OF_STUDY_TC_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_LEVEL_OF_STUDY_TC_VALUES!r}"
    )
