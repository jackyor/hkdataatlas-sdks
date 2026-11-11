from typing import Literal

RouteEtaResponseType = Literal["RouteETA"]

ROUTE_ETA_RESPONSE_TYPE_VALUES: set[RouteEtaResponseType] = {
    "RouteETA",
}


def check_route_eta_response_type(value: str) -> RouteEtaResponseType:
    if value in ROUTE_ETA_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_ETA_RESPONSE_TYPE_VALUES!r}"
    )
