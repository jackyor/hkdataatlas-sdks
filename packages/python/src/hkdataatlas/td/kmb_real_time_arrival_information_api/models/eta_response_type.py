from typing import Literal

EtaResponseType = Literal["ETA"]

ETA_RESPONSE_TYPE_VALUES: set[EtaResponseType] = {
    "ETA",
}


def check_eta_response_type(value: str) -> EtaResponseType:
    if value in ETA_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ETA_RESPONSE_TYPE_VALUES!r}"
    )
