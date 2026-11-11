from typing import Literal

GetClimateWeatherOpenDataDataType = Literal[
    "CLMMAXT", "CLMMINT", "CLMTEMP", "HHOT", "HLT", "LHL", "LTMV", "MRS", "RYES", "SRS"
]

GET_CLIMATE_WEATHER_OPEN_DATA_DATA_TYPE_VALUES: set[
    GetClimateWeatherOpenDataDataType
] = {
    "CLMMAXT",
    "CLMMINT",
    "CLMTEMP",
    "HHOT",
    "HLT",
    "LHL",
    "LTMV",
    "MRS",
    "RYES",
    "SRS",
}


def check_get_climate_weather_open_data_data_type(
    value: str,
) -> GetClimateWeatherOpenDataDataType:
    if value in GET_CLIMATE_WEATHER_OPEN_DATA_DATA_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CLIMATE_WEATHER_OPEN_DATA_DATA_TYPE_VALUES!r}"
    )
