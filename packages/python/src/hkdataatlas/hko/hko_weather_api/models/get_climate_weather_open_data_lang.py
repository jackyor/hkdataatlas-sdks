from typing import Literal

GetClimateWeatherOpenDataLang = Literal["en", "sc", "tc"]

GET_CLIMATE_WEATHER_OPEN_DATA_LANG_VALUES: set[GetClimateWeatherOpenDataLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_climate_weather_open_data_lang(
    value: str,
) -> GetClimateWeatherOpenDataLang:
    if value in GET_CLIMATE_WEATHER_OPEN_DATA_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CLIMATE_WEATHER_OPEN_DATA_LANG_VALUES!r}"
    )
