from typing import Literal

ListRoutesAction = Literal["list"]

LIST_ROUTES_ACTION_VALUES: set[ListRoutesAction] = {
    "list",
}


def check_list_routes_action(value: str) -> ListRoutesAction:
    if value in LIST_ROUTES_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ROUTES_ACTION_VALUES!r}"
    )
