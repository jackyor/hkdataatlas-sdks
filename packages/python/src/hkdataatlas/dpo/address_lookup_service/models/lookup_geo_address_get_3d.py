from typing import Literal

LookupGeoAddressGet3D = Literal[0, 1]

LOOKUP_GEO_ADDRESS_GET_3D_VALUES: set[LookupGeoAddressGet3D] = {
    0,
    1,
}


def check_lookup_geo_address_get_3d(value: int) -> LookupGeoAddressGet3D:
    if value in LOOKUP_GEO_ADDRESS_GET_3D_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOOKUP_GEO_ADDRESS_GET_3D_VALUES!r}"
    )
