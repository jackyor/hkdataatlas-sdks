from typing import Literal

GetCarparkInfoVacancyLang = Literal["en_US", "zh_CN", "zh_TW"]

GET_CARPARK_INFO_VACANCY_LANG_VALUES: set[GetCarparkInfoVacancyLang] = {
    "en_US",
    "zh_CN",
    "zh_TW",
}


def check_get_carpark_info_vacancy_lang(value: str) -> GetCarparkInfoVacancyLang:
    if value in GET_CARPARK_INFO_VACANCY_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CARPARK_INFO_VACANCY_LANG_VALUES!r}"
    )
