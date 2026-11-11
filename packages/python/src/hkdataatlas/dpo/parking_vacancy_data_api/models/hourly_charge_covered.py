from typing import Literal

HourlyChargeCovered = Literal["covered", "mixed", "open-air", "semi-covered"]

HOURLY_CHARGE_COVERED_VALUES: set[HourlyChargeCovered] = {
    "covered",
    "mixed",
    "open-air",
    "semi-covered",
}


def check_hourly_charge_covered(value: str) -> HourlyChargeCovered:
    if value in HOURLY_CHARGE_COVERED_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {HOURLY_CHARGE_COVERED_VALUES!r}"
    )
