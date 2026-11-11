from typing import Literal

Segment = Literal["Bills", "Notes"]

SEGMENT_VALUES: set[Segment] = {
    "Bills",
    "Notes",
}


def check_segment(value: str) -> Segment:
    if value in SEGMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEGMENT_VALUES!r}")
