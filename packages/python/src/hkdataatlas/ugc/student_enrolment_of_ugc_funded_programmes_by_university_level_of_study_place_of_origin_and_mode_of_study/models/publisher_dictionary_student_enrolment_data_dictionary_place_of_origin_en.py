from typing import Literal

PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginEN = Literal[
    "Local Student",
    "Other places of Asia",
    "The Mainland of China",
    "The rest of the world",
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_PLACE_OF_ORIGIN_EN_VALUES: set[
    PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginEN
] = {
    "Local Student",
    "Other places of Asia",
    "The Mainland of China",
    "The rest of the world",
}


def check_publisher_dictionary_student_enrolment_data_dictionary_place_of_origin_en(
    value: str,
) -> PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginEN:
    if (
        value
        in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_PLACE_OF_ORIGIN_EN_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_PLACE_OF_ORIGIN_EN_VALUES!r}"
    )
