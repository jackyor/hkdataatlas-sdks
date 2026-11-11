from typing import Literal

Segment = Literal["EUR", "USD"]

SEGMENT_VALUES: set[Segment] = {
    "EUR",
    "USD",
}


def check_segment(value: str) -> Segment:
    if value in SEGMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEGMENT_VALUES!r}")
