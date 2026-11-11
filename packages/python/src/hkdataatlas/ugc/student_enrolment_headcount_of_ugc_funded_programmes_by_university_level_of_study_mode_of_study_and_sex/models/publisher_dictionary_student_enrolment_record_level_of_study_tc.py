from typing import Literal

PublisherDictionaryStudentEnrolmentRecordLevelOfStudyTC = Literal[
    "副學位課程", "學士學位課程", "硏究院修課課程", "硏究院硏究課程"
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_LEVEL_OF_STUDY_TC_VALUES: set[
    PublisherDictionaryStudentEnrolmentRecordLevelOfStudyTC
] = {
    "副學位課程",
    "學士學位課程",
    "硏究院修課課程",
    "硏究院硏究課程",
}


def check_publisher_dictionary_student_enrolment_record_level_of_study_tc(
    value: str,
) -> PublisherDictionaryStudentEnrolmentRecordLevelOfStudyTC:
    if value in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_LEVEL_OF_STUDY_TC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_LEVEL_OF_STUDY_TC_VALUES!r}"
    )
