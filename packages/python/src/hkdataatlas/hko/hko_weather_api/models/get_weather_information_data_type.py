from typing import Literal

GetWeatherInformationDataType = Literal[
    "flw", "fnd", "rhrread", "swt", "warningInfo", "warnsum"
]

GET_WEATHER_INFORMATION_DATA_TYPE_VALUES: set[GetWeatherInformationDataType] = {
    "flw",
    "fnd",
    "rhrread",
    "swt",
    "warningInfo",
    "warnsum",
}


def check_get_weather_information_data_type(
    value: str,
) -> GetWeatherInformationDataType:
    if value in GET_WEATHER_INFORMATION_DATA_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_WEATHER_INFORMATION_DATA_TYPE_VALUES!r}"
    )
