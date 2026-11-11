from typing import Literal

RouteResponseType = Literal["Route"]

ROUTE_RESPONSE_TYPE_VALUES: set[RouteResponseType] = {
    "Route",
}


def check_route_response_type(value: str) -> RouteResponseType:
    if value in ROUTE_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_RESPONSE_TYPE_VALUES!r}"
    )
