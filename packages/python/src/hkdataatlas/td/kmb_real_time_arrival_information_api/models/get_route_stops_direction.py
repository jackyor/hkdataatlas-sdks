from typing import Literal

GetRouteStopsDirection = Literal["inbound", "outbound"]

GET_ROUTE_STOPS_DIRECTION_VALUES: set[GetRouteStopsDirection] = {
    "inbound",
    "outbound",
}


def check_get_route_stops_direction(value: str) -> GetRouteStopsDirection:
    if value in GET_ROUTE_STOPS_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ROUTE_STOPS_DIRECTION_VALUES!r}"
    )
