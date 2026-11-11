from typing import Literal

GetLocationAndProfileDataLang = Literal["en", "sc", "tc"]

GET_LOCATION_AND_PROFILE_DATA_LANG_VALUES: set[GetLocationAndProfileDataLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_location_and_profile_data_lang(
    value: str,
) -> GetLocationAndProfileDataLang:
    if value in GET_LOCATION_AND_PROFILE_DATA_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LOCATION_AND_PROFILE_DATA_LANG_VALUES!r}"
    )
