from typing import Literal

LookupGeoAddressGetAcceptEncoding = Literal["gzip"]

LOOKUP_GEO_ADDRESS_GET_ACCEPT_ENCODING_VALUES: set[
    LookupGeoAddressGetAcceptEncoding
] = {
    "gzip",
}


def check_lookup_geo_address_get_accept_encoding(
    value: str,
) -> LookupGeoAddressGetAcceptEncoding:
    if value in LOOKUP_GEO_ADDRESS_GET_ACCEPT_ENCODING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOOKUP_GEO_ADDRESS_GET_ACCEPT_ENCODING_VALUES!r}"
    )
