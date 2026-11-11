from typing import Literal

GetLastUpdateForRouteOrRouteSequenceRegionType0 = Literal["HKI", "KLN", "NT"]

GET_LAST_UPDATE_FOR_ROUTE_OR_ROUTE_SEQUENCE_REGION_TYPE_0_VALUES: set[
    GetLastUpdateForRouteOrRouteSequenceRegionType0
] = {
    "HKI",
    "KLN",
    "NT",
}


def check_get_last_update_for_route_or_route_sequence_region_type_0(
    value: str,
) -> GetLastUpdateForRouteOrRouteSequenceRegionType0:
    if value in GET_LAST_UPDATE_FOR_ROUTE_OR_ROUTE_SEQUENCE_REGION_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LAST_UPDATE_FOR_ROUTE_OR_ROUTE_SEQUENCE_REGION_TYPE_0_VALUES!r}"
    )
