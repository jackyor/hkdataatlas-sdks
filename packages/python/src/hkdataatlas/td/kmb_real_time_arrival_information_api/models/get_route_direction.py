from typing import Literal

GetRouteDirection = Literal["inbound", "outbound"]

GET_ROUTE_DIRECTION_VALUES: set[GetRouteDirection] = {
    "inbound",
    "outbound",
}


def check_get_route_direction(value: str) -> GetRouteDirection:
    if value in GET_ROUTE_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ROUTE_DIRECTION_VALUES!r}"
    )
