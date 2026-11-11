from typing import Literal

MonthlyChargeCovered = Literal["covered", "mixed", "open-air", "semi-covered"]

MONTHLY_CHARGE_COVERED_VALUES: set[MonthlyChargeCovered] = {
    "covered",
    "mixed",
    "open-air",
    "semi-covered",
}


def check_monthly_charge_covered(value: str) -> MonthlyChargeCovered:
    if value in MONTHLY_CHARGE_COVERED_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONTHLY_CHARGE_COVERED_VALUES!r}"
    )
