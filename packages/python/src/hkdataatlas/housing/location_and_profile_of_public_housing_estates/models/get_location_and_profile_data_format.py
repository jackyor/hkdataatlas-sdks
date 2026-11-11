from typing import Literal

GetLocationAndProfileDataFormat = Literal["csv", "json", "xml"]

GET_LOCATION_AND_PROFILE_DATA_FORMAT_VALUES: set[GetLocationAndProfileDataFormat] = {
    "csv",
    "json",
    "xml",
}


def check_get_location_and_profile_data_format(
    value: str,
) -> GetLocationAndProfileDataFormat:
    if value in GET_LOCATION_AND_PROFILE_DATA_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LOCATION_AND_PROFILE_DATA_FORMAT_VALUES!r}"
    )
