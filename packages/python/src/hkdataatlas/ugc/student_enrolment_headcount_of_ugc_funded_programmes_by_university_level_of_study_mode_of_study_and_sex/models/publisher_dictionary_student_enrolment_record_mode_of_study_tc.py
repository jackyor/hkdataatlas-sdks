from typing import Literal

PublisherDictionaryStudentEnrolmentRecordModeOfStudyTC = Literal["全日制", "兼讀制"]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_MODE_OF_STUDY_TC_VALUES: set[
    PublisherDictionaryStudentEnrolmentRecordModeOfStudyTC
] = {
    "全日制",
    "兼讀制",
}


def check_publisher_dictionary_student_enrolment_record_mode_of_study_tc(
    value: str,
) -> PublisherDictionaryStudentEnrolmentRecordModeOfStudyTC:
    if value in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_MODE_OF_STUDY_TC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_MODE_OF_STUDY_TC_VALUES!r}"
    )
