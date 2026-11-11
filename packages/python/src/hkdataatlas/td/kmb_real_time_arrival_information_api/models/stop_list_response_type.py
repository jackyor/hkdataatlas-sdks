from typing import Literal

StopListResponseType = Literal["StopList"]

STOP_LIST_RESPONSE_TYPE_VALUES: set[StopListResponseType] = {
    "StopList",
}


def check_stop_list_response_type(value: str) -> StopListResponseType:
    if value in STOP_LIST_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_LIST_RESPONSE_TYPE_VALUES!r}"
    )
