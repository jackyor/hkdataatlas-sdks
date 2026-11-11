from typing import Literal

GetHourlyRainfallLang = Literal["en", "sc", "tc"]

GET_HOURLY_RAINFALL_LANG_VALUES: set[GetHourlyRainfallLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_hourly_rainfall_lang(value: str) -> GetHourlyRainfallLang:
    if value in GET_HOURLY_RAINFALL_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOURLY_RAINFALL_LANG_VALUES!r}"
    )
