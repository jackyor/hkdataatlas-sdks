from typing import Literal

PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryEN = Literal[
    "Architecture and Town Planning",
    "Arts, Design and Performing Arts",
    "Biological Sciences",
    "Business and Management Studies",
    "Computer Science and Information Technology",
    "Dentistry",
    "Education",
    "Engineering and Technology",
    "Humanities",
    "Languages and Related Studies",
    "Law",
    "Mathematical Sciences",
    "Media, Journalism and Communications",
    "Medicine",
    "Physical Sciences",
    "Social Sciences",
    "Studies Allied to Medicine and Health",
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_ACADEMIC_PROGRAMME_CATEGORY_EN_VALUES: set[
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryEN
] = {
    "Architecture and Town Planning",
    "Arts, Design and Performing Arts",
    "Biological Sciences",
    "Business and Management Studies",
    "Computer Science and Information Technology",
    "Dentistry",
    "Education",
    "Engineering and Technology",
    "Humanities",
    "Languages and Related Studies",
    "Law",
    "Mathematical Sciences",
    "Media, Journalism and Communications",
    "Medicine",
    "Physical Sciences",
    "Social Sciences",
    "Studies Allied to Medicine and Health",
}


def check_publisher_dictionary_student_enrolment_headcount_data_dictionary_academic_programme_category_en(
    value: str,
) -> PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryEN:
    if (
        value
        in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_ACADEMIC_PROGRAMME_CATEGORY_EN_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_ACADEMIC_PROGRAMME_CATEGORY_EN_VALUES!r}"
    )
