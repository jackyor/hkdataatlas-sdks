from typing import Literal

RouteBound = Literal["I", "O"]

ROUTE_BOUND_VALUES: set[RouteBound] = {
    "I",
    "O",
}


def check_route_bound(value: str) -> RouteBound:
    if value in ROUTE_BOUND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_BOUND_VALUES!r}"
    )
