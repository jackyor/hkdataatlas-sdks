from typing import Literal

CarparkFacilitiesItem = Literal[
    "disabilities", "evCharger", "unloading", "valet-parking", "washing"
]

CARPARK_FACILITIES_ITEM_VALUES: set[CarparkFacilitiesItem] = {
    "disabilities",
    "evCharger",
    "unloading",
    "valet-parking",
    "washing",
}


def check_carpark_facilities_item(value: str) -> CarparkFacilitiesItem:
    if value in CARPARK_FACILITIES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CARPARK_FACILITIES_ITEM_VALUES!r}"
    )
