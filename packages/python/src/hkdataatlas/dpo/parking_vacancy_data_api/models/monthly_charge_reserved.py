from typing import Literal

MonthlyChargeReserved = Literal["non-reserved", "reserved"]

MONTHLY_CHARGE_RESERVED_VALUES: set[MonthlyChargeReserved] = {
    "non-reserved",
    "reserved",
}


def check_monthly_charge_reserved(value: str) -> MonthlyChargeReserved:
    if value in MONTHLY_CHARGE_RESERVED_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONTHLY_CHARGE_RESERVED_VALUES!r}"
    )
