from typing import Literal

PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginTC = Literal[
    "中國內地", "亞洲其他地區", "其他地區", "本地學生"
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_PLACE_OF_ORIGIN_TC_VALUES: set[
    PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginTC
] = {
    "中國內地",
    "亞洲其他地區",
    "其他地區",
    "本地學生",
}


def check_publisher_dictionary_student_enrolment_data_dictionary_place_of_origin_tc(
    value: str,
) -> PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginTC:
    if (
        value
        in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_PLACE_OF_ORIGIN_TC_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_DATA_DICTIONARY_PLACE_OF_ORIGIN_TC_VALUES!r}"
    )
