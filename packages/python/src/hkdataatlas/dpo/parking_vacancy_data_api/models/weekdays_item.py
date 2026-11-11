from typing import Literal

WeekdaysItem = Literal["FRI", "MON", "PH", "SAT", "SUN", "THU", "TUE", "WED"]

WEEKDAYS_ITEM_VALUES: set[WeekdaysItem] = {
    "FRI",
    "MON",
    "PH",
    "SAT",
    "SUN",
    "THU",
    "TUE",
    "WED",
}


def check_weekdays_item(value: str) -> WeekdaysItem:
    if value in WEEKDAYS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEEKDAYS_ITEM_VALUES!r}"
    )
