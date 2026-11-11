from typing import Literal

LookupAddressGet3D = Literal[0, 1]

LOOKUP_ADDRESS_GET_3D_VALUES: set[LookupAddressGet3D] = {
    0,
    1,
}


def check_lookup_address_get_3d(value: int) -> LookupAddressGet3D:
    if value in LOOKUP_ADDRESS_GET_3D_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOOKUP_ADDRESS_GET_3D_VALUES!r}"
    )
