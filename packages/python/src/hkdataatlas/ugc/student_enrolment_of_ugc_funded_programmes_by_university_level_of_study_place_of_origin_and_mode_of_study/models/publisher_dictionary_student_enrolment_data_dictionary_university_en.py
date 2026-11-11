from typing import Literal

PublisherDictionaryStudentEnrolmentDataDictionaryUniversityEN = Literal[
    "City University of Hong Kong",
    "Hong Kong Baptist University",
    "Lingnan University",
    "The Chinese University of Hong Kong",
    "The Education University of Hong Kong",
    "The Hong Kong Polytechnic University",
    "The Hong Kong University of Science and Technology",
    "The University of Hong Kong",
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_UNIVERSITY_EN_VALUES: set[
    PublisherDictionaryStudentEnrolmentDataDictionaryUniversityEN
] = {
    "City University of Hong Kong",
    "Hong Kong Baptist University",
    "Lingnan University",
    "The Chinese University of Hong Kong",
    "The Education University of Hong Kong",
    "The Hong Kong Polytechnic University",
    "The Hong Kong University of Science and Technology",
    "The University of Hong Kong",
}


def check_publisher_dictionary_student_enrolment_data_dictionary_university_en(
    value: str,
) -> PublisherDictionaryStudentEnrolmentDataDictionaryUniversityEN:
    if (
        value
        in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_UNIVERSITY_EN_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_UNIVERSITY_EN_VALUES!r}"
    )
