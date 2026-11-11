from typing import Literal

GetAedInformationLang = Literal["EN", "SC", "TC"]

GET_AED_INFORMATION_LANG_VALUES: set[GetAedInformationLang] = {
    "EN",
    "SC",
    "TC",
}


def check_get_aed_information_lang(value: str) -> GetAedInformationLang:
    if value in GET_AED_INFORMATION_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_AED_INFORMATION_LANG_VALUES!r}"
    )
