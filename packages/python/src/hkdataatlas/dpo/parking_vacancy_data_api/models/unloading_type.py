from typing import Literal

UnloadingType = Literal["half-hourly", "hourly"]

UNLOADING_TYPE_VALUES: set[UnloadingType] = {
    "half-hourly",
    "hourly",
}


def check_unloading_type(value: str) -> UnloadingType:
    if value in UNLOADING_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UNLOADING_TYPE_VALUES!r}"
    )
