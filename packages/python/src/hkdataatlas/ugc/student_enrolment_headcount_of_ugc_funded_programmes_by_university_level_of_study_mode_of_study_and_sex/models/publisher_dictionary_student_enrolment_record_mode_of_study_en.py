from typing import Literal

PublisherDictionaryStudentEnrolmentRecordModeOfStudyEN = Literal[
    "Full-time", "Part-time"
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_MODE_OF_STUDY_EN_VALUES: set[
    PublisherDictionaryStudentEnrolmentRecordModeOfStudyEN
] = {
    "Full-time",
    "Part-time",
}


def check_publisher_dictionary_student_enrolment_record_mode_of_study_en(
    value: str,
) -> PublisherDictionaryStudentEnrolmentRecordModeOfStudyEN:
    if value in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_MODE_OF_STUDY_EN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_MODE_OF_STUDY_EN_VALUES!r}"
    )
