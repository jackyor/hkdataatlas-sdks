from typing import Literal

UnloadingChargeType = Literal["half-hourly", "hourly"]

UNLOADING_CHARGE_TYPE_VALUES: set[UnloadingChargeType] = {
    "half-hourly",
    "hourly",
}


def check_unloading_charge_type(value: str) -> UnloadingChargeType:
    if value in UNLOADING_CHARGE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UNLOADING_CHARGE_TYPE_VALUES!r}"
    )
