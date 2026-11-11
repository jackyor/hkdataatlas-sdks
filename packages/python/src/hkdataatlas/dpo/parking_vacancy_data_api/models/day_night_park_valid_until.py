from typing import Literal

DayNightParkValidUntil = Literal["following-day", "no-restrictions", "same-day"]

DAY_NIGHT_PARK_VALID_UNTIL_VALUES: set[DayNightParkValidUntil] = {
    "following-day",
    "no-restrictions",
    "same-day",
}


def check_day_night_park_valid_until(value: str) -> DayNightParkValidUntil:
    if value in DAY_NIGHT_PARK_VALID_UNTIL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DAY_NIGHT_PARK_VALID_UNTIL_VALUES!r}"
    )
