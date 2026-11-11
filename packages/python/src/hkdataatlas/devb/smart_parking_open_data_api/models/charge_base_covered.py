from typing import Literal

ChargeBaseCovered = Literal["covered", "mixed", "open-air", "semi-covered"]

CHARGE_BASE_COVERED_VALUES: set[ChargeBaseCovered] = {
    "covered",
    "mixed",
    "open-air",
    "semi-covered",
}


def check_charge_base_covered(value: str) -> ChargeBaseCovered:
    if value in CHARGE_BASE_COVERED_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHARGE_BASE_COVERED_VALUES!r}"
    )
