from typing import Literal

LookupGeoAddressGetAccept = Literal["application/json", "application/xml"]

LOOKUP_GEO_ADDRESS_GET_ACCEPT_VALUES: set[LookupGeoAddressGetAccept] = {
    "application/json",
    "application/xml",
}


def check_lookup_geo_address_get_accept(value: str) -> LookupGeoAddressGetAccept:
    if value in LOOKUP_GEO_ADDRESS_GET_ACCEPT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOOKUP_GEO_ADDRESS_GET_ACCEPT_VALUES!r}"
    )
