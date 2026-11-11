from typing import Literal

RoutesRegionalResponseType = Literal["Routes-Regional"]

ROUTES_REGIONAL_RESPONSE_TYPE_VALUES: set[RoutesRegionalResponseType] = {
    "Routes-Regional",
}


def check_routes_regional_response_type(value: str) -> RoutesRegionalResponseType:
    if value in ROUTES_REGIONAL_RESPONSE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTES_REGIONAL_RESPONSE_TYPE_VALUES!r}"
    )
