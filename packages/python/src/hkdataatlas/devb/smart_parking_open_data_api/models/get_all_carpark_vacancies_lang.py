from typing import Literal

GetAllCarparkVacanciesLang = Literal["en_US", "zh_TW"]

GET_ALL_CARPARK_VACANCIES_LANG_VALUES: set[GetAllCarparkVacanciesLang] = {
    "en_US",
    "zh_TW",
}


def check_get_all_carpark_vacancies_lang(value: str) -> GetAllCarparkVacanciesLang:
    if value in GET_ALL_CARPARK_VACANCIES_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ALL_CARPARK_VACANCIES_LANG_VALUES!r}"
    )
