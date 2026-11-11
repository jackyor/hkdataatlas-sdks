from typing import Literal

StopRouteResponseType = Literal["StopRoute"]

STOP_ROUTE_RESPONSE_TYPE_VALUES: set[StopRouteResponseType] = {
    "StopRoute",
}


def check_stop_route_response_type(value: str) -> StopRouteResponseType:
    if value in STOP_ROUTE_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ROUTE_RESPONSE_TYPE_VALUES!r}"
    )
