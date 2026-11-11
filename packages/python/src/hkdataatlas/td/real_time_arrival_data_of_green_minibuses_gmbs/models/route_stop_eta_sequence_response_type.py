from typing import Literal

RouteStopEtaSequenceResponseType = Literal["ETA-Route-Stop"]

ROUTE_STOP_ETA_SEQUENCE_RESPONSE_TYPE_VALUES: set[RouteStopEtaSequenceResponseType] = {
    "ETA-Route-Stop",
}


def check_route_stop_eta_sequence_response_type(
    value: str,
) -> RouteStopEtaSequenceResponseType:
    if value in ROUTE_STOP_ETA_SEQUENCE_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_STOP_ETA_SEQUENCE_RESPONSE_TYPE_VALUES!r}"
    )
