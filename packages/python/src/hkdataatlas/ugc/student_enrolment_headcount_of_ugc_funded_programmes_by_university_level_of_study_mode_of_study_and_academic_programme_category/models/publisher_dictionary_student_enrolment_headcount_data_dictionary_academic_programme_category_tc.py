from typing import Literal

PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryTC = Literal[
    "人文學科",
    "媒體、新聞及傳播",
    "工商管理",
    "工程及科技",
    "建築學及城市規劃",
    "教育",
    "數學科學",
    "法律",
    "牙醫學",
    "物理科學",
    "生物科學",
    "社會科學",
    "與醫學及衛生有關的學科",
    "藝術、設計及演藝",
    "語言及相關科目",
    "醫學",
    "電腦科學及資訊科技",
]

PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_ACADEMIC_PROGRAMME_CATEGORY_TC_VALUES: set[
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryTC
] = {
    "人文學科",
    "媒體、新聞及傳播",
    "工商管理",
    "工程及科技",
    "建築學及城市規劃",
    "教育",
    "數學科學",
    "法律",
    "牙醫學",
    "物理科學",
    "生物科學",
    "社會科學",
    "與醫學及衛生有關的學科",
    "藝術、設計及演藝",
    "語言及相關科目",
    "醫學",
    "電腦科學及資訊科技",
}


def check_publisher_dictionary_student_enrolment_headcount_data_dictionary_academic_programme_category_tc(
    value: str,
) -> PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryTC:
    if (
        value
        in PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_ACADEMIC_PROGRAMME_CATEGORY_TC_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISHER_DICTIONARY_STUDENT_ENROLMENT_HEADCOUNT_DATA_DICTIONARY_ACADEMIC_PROGRAMME_CATEGORY_TC_VALUES!r}"
    )
