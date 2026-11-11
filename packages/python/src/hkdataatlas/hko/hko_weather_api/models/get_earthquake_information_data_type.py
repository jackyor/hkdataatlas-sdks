from typing import Literal

GetEarthquakeInformationDataType = Literal["feltearthquake", "qem"]

GET_EARTHQUAKE_INFORMATION_DATA_TYPE_VALUES: set[GetEarthquakeInformationDataType] = {
    "feltearthquake",
    "qem",
}


def check_get_earthquake_information_data_type(
    value: str,
) -> GetEarthquakeInformationDataType:
    if value in GET_EARTHQUAKE_INFORMATION_DATA_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_EARTHQUAKE_INFORMATION_DATA_TYPE_VALUES!r}"
    )
