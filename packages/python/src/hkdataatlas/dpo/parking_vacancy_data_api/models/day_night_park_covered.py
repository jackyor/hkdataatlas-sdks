from typing import Literal

DayNightParkCovered = Literal["covered", "mixed", "open-air", "semi-covered"]

DAY_NIGHT_PARK_COVERED_VALUES: set[DayNightParkCovered] = {
    "covered",
    "mixed",
    "open-air",
    "semi-covered",
}


def check_day_night_park_covered(value: str) -> DayNightParkCovered:
    if value in DAY_NIGHT_PARK_COVERED_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DAY_NIGHT_PARK_COVERED_VALUES!r}"
    )
