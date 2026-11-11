from typing import Literal

GetEarthquakeInformationLang = Literal["en", "sc", "tc"]

GET_EARTHQUAKE_INFORMATION_LANG_VALUES: set[GetEarthquakeInformationLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_earthquake_information_lang(value: str) -> GetEarthquakeInformationLang:
    if value in GET_EARTHQUAKE_INFORMATION_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EARTHQUAKE_INFORMATION_LANG_VALUES!r}"
    )
