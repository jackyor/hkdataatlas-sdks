from typing import Literal

LastUpdateSingleResponseType = Literal["Last-Update"]

LAST_UPDATE_SINGLE_RESPONSE_TYPE_VALUES: set[LastUpdateSingleResponseType] = {
    "Last-Update",
}


def check_last_update_single_response_type(value: str) -> LastUpdateSingleResponseType:
    if value in LAST_UPDATE_SINGLE_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LAST_UPDATE_SINGLE_RESPONSE_TYPE_VALUES!r}"
    )
