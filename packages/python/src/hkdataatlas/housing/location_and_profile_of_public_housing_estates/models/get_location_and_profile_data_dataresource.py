from typing import Literal

GetLocationAndProfileDataDataresource = Literal[
    "flatted-factory", "hos-courts", "prh-estates", "shopping-centres"
]

GET_LOCATION_AND_PROFILE_DATA_DATARESOURCE_VALUES: set[
    GetLocationAndProfileDataDataresource
] = {
    "flatted-factory",
    "hos-courts",
    "prh-estates",
    "shopping-centres",
}


def check_get_location_and_profile_data_dataresource(
    value: str,
) -> GetLocationAndProfileDataDataresource:
    if value in GET_LOCATION_AND_PROFILE_DATA_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LOCATION_AND_PROFILE_DATA_DATARESOURCE_VALUES!r}"
    )
