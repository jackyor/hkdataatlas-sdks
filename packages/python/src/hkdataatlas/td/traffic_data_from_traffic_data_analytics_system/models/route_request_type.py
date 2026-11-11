from typing import Literal

RouteRequestType = Literal["SD", "ST"]

ROUTE_REQUEST_TYPE_VALUES: set[RouteRequestType] = {
    "SD",
    "ST",
}


def check_route_request_type(value: str) -> RouteRequestType:
    if value in ROUTE_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_REQUEST_TYPE_VALUES!r}"
    )
