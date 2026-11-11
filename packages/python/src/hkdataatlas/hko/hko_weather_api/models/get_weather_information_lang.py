from typing import Literal

GetWeatherInformationLang = Literal["en", "sc", "tc"]

GET_WEATHER_INFORMATION_LANG_VALUES: set[GetWeatherInformationLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_weather_information_lang(value: str) -> GetWeatherInformationLang:
    if value in GET_WEATHER_INFORMATION_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WEATHER_INFORMATION_LANG_VALUES!r}"
    )
