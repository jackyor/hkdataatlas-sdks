from typing import Literal

GetCitybusRouteStopsDirection = Literal["inbound", "outbound"]

GET_CITYBUS_ROUTE_STOPS_DIRECTION_VALUES: set[GetCitybusRouteStopsDirection] = {
    "inbound",
    "outbound",
}


def check_get_citybus_route_stops_direction(
    value: str,
) -> GetCitybusRouteStopsDirection:
    if value in GET_CITYBUS_ROUTE_STOPS_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CITYBUS_ROUTE_STOPS_DIRECTION_VALUES!r}"
    )
