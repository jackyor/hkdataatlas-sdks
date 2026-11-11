from typing import Literal

LookupAddressGetB = Literal[0, 1]

LOOKUP_ADDRESS_GET_B_VALUES: set[LookupAddressGetB] = {
    0,
    1,
}


def check_lookup_address_get_b(value: int) -> LookupAddressGetB:
    if value in LOOKUP_ADDRESS_GET_B_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOOKUP_ADDRESS_GET_B_VALUES!r}"
    )
