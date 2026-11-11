from typing import Literal

Segment = Literal["182day", "28day", "364day", "91day"]

SEGMENT_VALUES: set[Segment] = {
    "182day",
    "28day",
    "364day",
    "91day",
}


def check_segment(value: str) -> Segment:
    if value in SEGMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEGMENT_VALUES!r}")
