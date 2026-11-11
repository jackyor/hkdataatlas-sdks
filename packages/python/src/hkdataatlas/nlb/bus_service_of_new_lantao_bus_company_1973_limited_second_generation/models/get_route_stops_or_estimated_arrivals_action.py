from typing import Literal

GetRouteStopsOrEstimatedArrivalsAction = Literal["estimatedArrivals", "list"]

GET_ROUTE_STOPS_OR_ESTIMATED_ARRIVALS_ACTION_VALUES: set[
    GetRouteStopsOrEstimatedArrivalsAction
] = {
    "estimatedArrivals",
    "list",
}


def check_get_route_stops_or_estimated_arrivals_action(
    value: str,
) -> GetRouteStopsOrEstimatedArrivalsAction:
    if value in GET_ROUTE_STOPS_OR_ESTIMATED_ARRIVALS_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ROUTE_STOPS_OR_ESTIMATED_ARRIVALS_ACTION_VALUES!r}"
    )
