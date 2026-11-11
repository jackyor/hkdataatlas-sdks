from typing import Literal

RouteStopEtaByStopIdResponseType = Literal["ETA-Route-Stop"]

ROUTE_STOP_ETA_BY_STOP_ID_RESPONSE_TYPE_VALUES: set[
    RouteStopEtaByStopIdResponseType
] = {
    "ETA-Route-Stop",
}


def check_route_stop_eta_by_stop_id_response_type(
    value: str,
) -> RouteStopEtaByStopIdResponseType:
    if value in ROUTE_STOP_ETA_BY_STOP_ID_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_STOP_ETA_BY_STOP_ID_RESPONSE_TYPE_VALUES!r}"
    )
