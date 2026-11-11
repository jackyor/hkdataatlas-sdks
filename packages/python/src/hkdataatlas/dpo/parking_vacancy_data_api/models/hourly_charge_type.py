from typing import Literal

HourlyChargeType = Literal["half-hourly", "hourly"]

HOURLY_CHARGE_TYPE_VALUES: set[HourlyChargeType] = {
    "half-hourly",
    "hourly",
}


def check_hourly_charge_type(value: str) -> HourlyChargeType:
    if value in HOURLY_CHARGE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {HOURLY_CHARGE_TYPE_VALUES!r}"
    )
