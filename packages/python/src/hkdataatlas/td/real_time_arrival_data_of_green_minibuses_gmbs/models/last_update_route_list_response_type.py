from typing import Literal

LastUpdateRouteListResponseType = Literal["Last-Update"]

LAST_UPDATE_ROUTE_LIST_RESPONSE_TYPE_VALUES: set[LastUpdateRouteListResponseType] = {
    "Last-Update",
}


def check_last_update_route_list_response_type(
    value: str,
) -> LastUpdateRouteListResponseType:
    if value in LAST_UPDATE_ROUTE_LIST_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LAST_UPDATE_ROUTE_LIST_RESPONSE_TYPE_VALUES!r}"
    )
