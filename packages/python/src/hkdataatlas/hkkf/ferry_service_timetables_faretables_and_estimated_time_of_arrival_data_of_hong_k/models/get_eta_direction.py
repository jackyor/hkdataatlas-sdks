from typing import Literal

GetEtaDirection = Literal["inbound", "outbound"]

GET_ETA_DIRECTION_VALUES: set[GetEtaDirection] = {
    "inbound",
    "outbound",
}


def check_get_eta_direction(value: str) -> GetEtaDirection:
    if value in GET_ETA_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ETA_DIRECTION_VALUES!r}"
    )
