from typing import Literal

GetRegionalRoutesOrRouteByIdRegionType0 = Literal["HKI", "KLN", "NT"]

GET_REGIONAL_ROUTES_OR_ROUTE_BY_ID_REGION_TYPE_0_VALUES: set[
    GetRegionalRoutesOrRouteByIdRegionType0
] = {
    "HKI",
    "KLN",
    "NT",
}


def check_get_regional_routes_or_route_by_id_region_type_0(
    value: str,
) -> GetRegionalRoutesOrRouteByIdRegionType0:
    if value in GET_REGIONAL_ROUTES_OR_ROUTE_BY_ID_REGION_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_REGIONAL_ROUTES_OR_ROUTE_BY_ID_REGION_TYPE_0_VALUES!r}"
    )
