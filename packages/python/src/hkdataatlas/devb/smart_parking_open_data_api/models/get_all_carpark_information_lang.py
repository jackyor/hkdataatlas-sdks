from typing import Literal

GetAllCarparkInformationLang = Literal["en_US", "zh_TW"]

GET_ALL_CARPARK_INFORMATION_LANG_VALUES: set[GetAllCarparkInformationLang] = {
    "en_US",
    "zh_TW",
}


def check_get_all_carpark_information_lang(value: str) -> GetAllCarparkInformationLang:
    if value in GET_ALL_CARPARK_INFORMATION_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ALL_CARPARK_INFORMATION_LANG_VALUES!r}"
    )
