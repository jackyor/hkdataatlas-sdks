from typing import Literal

ChiPremisesAddressRegion = Literal["九龍", "新界", "香港"]

CHI_PREMISES_ADDRESS_REGION_VALUES: set[ChiPremisesAddressRegion] = {
    "九龍",
    "新界",
    "香港",
}


def check_chi_premises_address_region(value: str) -> ChiPremisesAddressRegion:
    if value in CHI_PREMISES_ADDRESS_REGION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHI_PREMISES_ADDRESS_REGION_VALUES!r}"
    )
