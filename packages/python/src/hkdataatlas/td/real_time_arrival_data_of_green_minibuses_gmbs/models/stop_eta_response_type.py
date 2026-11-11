from typing import Literal

StopEtaResponseType = Literal["ETA-Stop"]

STOP_ETA_RESPONSE_TYPE_VALUES: set[StopEtaResponseType] = {
    "ETA-Stop",
}


def check_stop_eta_response_type(value: str) -> StopEtaResponseType:
    if value in STOP_ETA_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ETA_RESPONSE_TYPE_VALUES!r}"
    )
