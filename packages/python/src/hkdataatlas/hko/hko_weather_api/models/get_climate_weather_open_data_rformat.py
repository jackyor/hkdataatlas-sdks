from typing import Literal

GetClimateWeatherOpenDataRformat = Literal["csv", "json"]

GET_CLIMATE_WEATHER_OPEN_DATA_RFORMAT_VALUES: set[GetClimateWeatherOpenDataRformat] = {
    "csv",
    "json",
}


def check_get_climate_weather_open_data_rformat(
    value: str,
) -> GetClimateWeatherOpenDataRformat:
    if value in GET_CLIMATE_WEATHER_OPEN_DATA_RFORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CLIMATE_WEATHER_OPEN_DATA_RFORMAT_VALUES!r}"
    )
