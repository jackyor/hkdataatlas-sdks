from typing import Literal

GetCarparkInformationLang = Literal["en_US", "zh_TW"]

GET_CARPARK_INFORMATION_LANG_VALUES: set[GetCarparkInformationLang] = {
    "en_US",
    "zh_TW",
}


def check_get_carpark_information_lang(value: str) -> GetCarparkInformationLang:
    if value in GET_CARPARK_INFORMATION_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CARPARK_INFORMATION_LANG_VALUES!r}"
    )
