from typing import Literal

GetRouteStopsOrEstimatedArrivalsLanguage = Literal["cn", "en", "zh"]

GET_ROUTE_STOPS_OR_ESTIMATED_ARRIVALS_LANGUAGE_VALUES: set[
    GetRouteStopsOrEstimatedArrivalsLanguage
] = {
    "cn",
    "en",
    "zh",
}


def check_get_route_stops_or_estimated_arrivals_language(
    value: str,
) -> GetRouteStopsOrEstimatedArrivalsLanguage:
    if value in GET_ROUTE_STOPS_OR_ESTIMATED_ARRIVALS_LANGUAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ROUTE_STOPS_OR_ESTIMATED_ARRIVALS_LANGUAGE_VALUES!r}"
    )
