from typing import Literal

RouteStopBound = Literal["I", "O"]

ROUTE_STOP_BOUND_VALUES: set[RouteStopBound] = {
    "I",
    "O",
}


def check_route_stop_bound(value: str) -> RouteStopBound:
    if value in ROUTE_STOP_BOUND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_STOP_BOUND_VALUES!r}"
    )
