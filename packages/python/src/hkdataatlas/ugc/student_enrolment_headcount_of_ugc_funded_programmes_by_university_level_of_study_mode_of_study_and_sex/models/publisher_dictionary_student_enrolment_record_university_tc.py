from typing import Literal

PublisherDictionaryStudentEnrolmentRecordUniversityTC = Literal[
    "嶺南大學",
    "香港中文大學",
    "香港城市大學",
    "香港大學",
    "香港教育大學",
    "香港浸會大學",
    "香港理工大學",
    "香港科技大學",
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_UNIVERSITY_TC_VALUES: set[
    PublisherDictionaryStudentEnrolmentRecordUniversityTC
] = {
    "嶺南大學",
    "香港中文大學",
    "香港城市大學",
    "香港大學",
    "香港教育大學",
    "香港浸會大學",
    "香港理工大學",
    "香港科技大學",
}


def check_publisher_dictionary_student_enrolment_record_university_tc(
    value: str,
) -> PublisherDictionaryStudentEnrolmentRecordUniversityTC:
    if value in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_UNIVERSITY_TC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_RECORD_UNIVERSITY_TC_VALUES!r}"
    )
