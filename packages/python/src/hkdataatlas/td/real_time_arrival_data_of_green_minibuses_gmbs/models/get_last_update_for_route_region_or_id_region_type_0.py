from typing import Literal

GetLastUpdateForRouteRegionOrIdRegionType0 = Literal["HKI", "KLN", "NT"]

GET_LAST_UPDATE_FOR_ROUTE_REGION_OR_ID_REGION_TYPE_0_VALUES: set[
    GetLastUpdateForRouteRegionOrIdRegionType0
] = {
    "HKI",
    "KLN",
    "NT",
}


def check_get_last_update_for_route_region_or_id_region_type_0(
    value: str,
) -> GetLastUpdateForRouteRegionOrIdRegionType0:
    if value in GET_LAST_UPDATE_FOR_ROUTE_REGION_OR_ID_REGION_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LAST_UPDATE_FOR_ROUTE_REGION_OR_ID_REGION_TYPE_0_VALUES!r}"
    )
