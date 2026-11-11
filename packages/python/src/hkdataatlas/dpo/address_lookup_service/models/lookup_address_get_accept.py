from typing import Literal

LookupAddressGetAccept = Literal["application/json", "application/xml"]

LOOKUP_ADDRESS_GET_ACCEPT_VALUES: set[LookupAddressGetAccept] = {
    "application/json",
    "application/xml",
}


def check_lookup_address_get_accept(value: str) -> LookupAddressGetAccept:
    if value in LOOKUP_ADDRESS_GET_ACCEPT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOOKUP_ADDRESS_GET_ACCEPT_VALUES!r}"
    )
