from typing import Literal

LastUpdateStopListResponseType = Literal["Last-Update"]

LAST_UPDATE_STOP_LIST_RESPONSE_TYPE_VALUES: set[LastUpdateStopListResponseType] = {
    "Last-Update",
}


def check_last_update_stop_list_response_type(
    value: str,
) -> LastUpdateStopListResponseType:
    if value in LAST_UPDATE_STOP_LIST_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LAST_UPDATE_STOP_LIST_RESPONSE_TYPE_VALUES!r}"
    )
