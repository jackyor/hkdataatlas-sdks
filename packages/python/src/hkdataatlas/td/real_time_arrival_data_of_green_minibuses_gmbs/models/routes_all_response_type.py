from typing import Literal

RoutesAllResponseType = Literal["Routes-All"]

ROUTES_ALL_RESPONSE_TYPE_VALUES: set[RoutesAllResponseType] = {
    "Routes-All",
}


def check_routes_all_response_type(value: str) -> RoutesAllResponseType:
    if value in ROUTES_ALL_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTES_ALL_RESPONSE_TYPE_VALUES!r}"
    )
