from typing import Literal

DayNightParkType = Literal[
    "12-hours-park", "24-hours-park", "6-hours-park", "day-park", "night-park"
]

DAY_NIGHT_PARK_TYPE_VALUES: set[DayNightParkType] = {
    "12-hours-park",
    "24-hours-park",
    "6-hours-park",
    "day-park",
    "night-park",
}


def check_day_night_park_type(value: str) -> DayNightParkType:
    if value in DAY_NIGHT_PARK_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DAY_NIGHT_PARK_TYPE_VALUES!r}"
    )
