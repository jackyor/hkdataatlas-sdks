from typing import Literal

PublisherDictionaryStudentEnrolmentRecordSexTC = Literal["女", "男"]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_SEX_TC_VALUES: set[
    PublisherDictionaryStudentEnrolmentRecordSexTC
] = {
    "女",
    "男",
}


def check_publisher_dictionary_student_enrolment_record_sex_tc(
    value: str,
) -> PublisherDictionaryStudentEnrolmentRecordSexTC:
    if value in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_SEX_TC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_SEX_TC_VALUES!r}"
    )
