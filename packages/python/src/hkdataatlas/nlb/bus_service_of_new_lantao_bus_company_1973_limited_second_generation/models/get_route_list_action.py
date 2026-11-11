from typing import Literal

GetRouteListAction = Literal["list"]

GET_ROUTE_LIST_ACTION_VALUES: set[GetRouteListAction] = {
    "list",
}


def check_get_route_list_action(value: str) -> GetRouteListAction:
    if value in GET_ROUTE_LIST_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ROUTE_LIST_ACTION_VALUES!r}"
    )
