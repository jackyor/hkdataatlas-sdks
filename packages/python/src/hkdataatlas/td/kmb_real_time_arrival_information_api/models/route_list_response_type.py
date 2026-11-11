from typing import Literal

RouteListResponseType = Literal["RouteList"]

ROUTE_LIST_RESPONSE_TYPE_VALUES: set[RouteListResponseType] = {
    "RouteList",
}


def check_route_list_response_type(value: str) -> RouteListResponseType:
    if value in ROUTE_LIST_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_LIST_RESPONSE_TYPE_VALUES!r}"
    )
