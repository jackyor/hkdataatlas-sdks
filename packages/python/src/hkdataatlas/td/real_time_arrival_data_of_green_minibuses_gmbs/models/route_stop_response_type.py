from typing import Literal

RouteStopResponseType = Literal["Route-Stop"]

ROUTE_STOP_RESPONSE_TYPE_VALUES: set[RouteStopResponseType] = {
    "Route-Stop",
}


def check_route_stop_response_type(value: str) -> RouteStopResponseType:
    if value in ROUTE_STOP_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_STOP_RESPONSE_TYPE_VALUES!r}"
    )
