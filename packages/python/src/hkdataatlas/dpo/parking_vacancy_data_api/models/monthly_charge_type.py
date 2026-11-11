from typing import Literal

MonthlyChargeType = Literal[
    "bimonthly-day-park",
    "bimonthly-night-park",
    "bimonthly-park",
    "monthly-day-park",
    "monthly-night-park",
    "monthly-park",
    "quarterly-day-park",
    "quarterly-night-park",
    "quarterly-park",
    "yearly-day-park",
    "yearly-night-park",
    "yearly-park",
]

MONTHLY_CHARGE_TYPE_VALUES: set[MonthlyChargeType] = {
    "bimonthly-day-park",
    "bimonthly-night-park",
    "bimonthly-park",
    "monthly-day-park",
    "monthly-night-park",
    "monthly-park",
    "quarterly-day-park",
    "quarterly-night-park",
    "quarterly-park",
    "yearly-day-park",
    "yearly-night-park",
    "yearly-park",
}


def check_monthly_charge_type(value: str) -> MonthlyChargeType:
    if value in MONTHLY_CHARGE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONTHLY_CHARGE_TYPE_VALUES!r}"
    )
