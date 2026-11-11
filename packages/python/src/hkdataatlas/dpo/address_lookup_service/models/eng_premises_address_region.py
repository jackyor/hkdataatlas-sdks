from typing import Literal

EngPremisesAddressRegion = Literal["HK", "KLN", "NT"]

ENG_PREMISES_ADDRESS_REGION_VALUES: set[EngPremisesAddressRegion] = {
    "HK",
    "KLN",
    "NT",
}


def check_eng_premises_address_region(value: str) -> EngPremisesAddressRegion:
    if value in ENG_PREMISES_ADDRESS_REGION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENG_PREMISES_ADDRESS_REGION_VALUES!r}"
    )
