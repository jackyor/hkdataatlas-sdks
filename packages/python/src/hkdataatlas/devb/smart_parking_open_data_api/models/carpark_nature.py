from typing import Literal

CarparkNature = Literal["commercial", "government"]

CARPARK_NATURE_VALUES: set[CarparkNature] = {
    "commercial",
    "government",
}


def check_carpark_nature(value: str) -> CarparkNature:
    if value in CARPARK_NATURE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CARPARK_NATURE_VALUES!r}"
    )
