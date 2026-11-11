from typing import Literal

LookupAddressGetAcceptEncoding = Literal["gzip"]

LOOKUP_ADDRESS_GET_ACCEPT_ENCODING_VALUES: set[LookupAddressGetAcceptEncoding] = {
    "gzip",
}


def check_lookup_address_get_accept_encoding(
    value: str,
) -> LookupAddressGetAcceptEncoding:
    if value in LOOKUP_ADDRESS_GET_ACCEPT_ENCODING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOOKUP_ADDRESS_GET_ACCEPT_ENCODING_VALUES!r}"
    )
