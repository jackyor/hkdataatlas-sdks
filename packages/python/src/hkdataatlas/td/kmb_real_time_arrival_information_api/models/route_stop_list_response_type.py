from typing import Literal

RouteStopListResponseType = Literal["RouteStopList"]

ROUTE_STOP_LIST_RESPONSE_TYPE_VALUES: set[RouteStopListResponseType] = {
    "RouteStopList",
}


def check_route_stop_list_response_type(value: str) -> RouteStopListResponseType:
    if value in ROUTE_STOP_LIST_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_STOP_LIST_RESPONSE_TYPE_VALUES!r}"
    )
