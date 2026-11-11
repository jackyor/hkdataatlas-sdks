from typing import Literal

StopResponseType = Literal["Stop"]

STOP_RESPONSE_TYPE_VALUES: set[StopResponseType] = {
    "Stop",
}


def check_stop_response_type(value: str) -> StopResponseType:
    if value in STOP_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_RESPONSE_TYPE_VALUES!r}"
    )
