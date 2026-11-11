from typing import Literal

CarparkType = Literal["metered", "multi-storey", "off-street"]

CARPARK_TYPE_VALUES: set[CarparkType] = {
    "metered",
    "multi-storey",
    "off-street",
}


def check_carpark_type(value: str) -> CarparkType:
    if value in CARPARK_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CARPARK_TYPE_VALUES!r}"
    )
