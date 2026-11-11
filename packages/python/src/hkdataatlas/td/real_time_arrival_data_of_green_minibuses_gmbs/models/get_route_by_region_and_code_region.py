from typing import Literal

GetRouteByRegionAndCodeRegion = Literal["HKI", "KLN", "NT"]

GET_ROUTE_BY_REGION_AND_CODE_REGION_VALUES: set[GetRouteByRegionAndCodeRegion] = {
    "HKI",
    "KLN",
    "NT",
}


def check_get_route_by_region_and_code_region(
    value: str,
) -> GetRouteByRegionAndCodeRegion:
    if value in GET_ROUTE_BY_REGION_AND_CODE_REGION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ROUTE_BY_REGION_AND_CODE_REGION_VALUES!r}"
    )
