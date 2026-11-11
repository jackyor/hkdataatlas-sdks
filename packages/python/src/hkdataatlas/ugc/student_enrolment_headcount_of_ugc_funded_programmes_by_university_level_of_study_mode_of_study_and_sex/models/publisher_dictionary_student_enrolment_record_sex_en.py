from typing import Literal

PublisherDictionaryStudentEnrolmentRecordSexEN = Literal["Female", "Male"]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_SEX_EN_VALUES: set[
    PublisherDictionaryStudentEnrolmentRecordSexEN
] = {
    "Female",
    "Male",
}


def check_publisher_dictionary_student_enrolment_record_sex_en(
    value: str,
) -> PublisherDictionaryStudentEnrolmentRecordSexEN:
    if value in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_SEX_EN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_SEX_EN_VALUES!r}"
    )
