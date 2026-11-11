from typing import Literal

Segment = Literal["10year", "15year", "2year", "3year", "5year", "7year"]

SEGMENT_VALUES: set[Segment] = {
    "10year",
    "15year",
    "2year",
    "3year",
    "5year",
    "7year",
}


def check_segment(value: str) -> Segment:
    if value in SEGMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEGMENT_VALUES!r}")
