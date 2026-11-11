from typing import Literal

Segment = Literal["LBIssuingSVF", "LBNotIssuingSVF", "SVFLic"]

SEGMENT_VALUES: set[Segment] = {
    "LBIssuingSVF",
    "LBNotIssuingSVF",
    "SVFLic",
}


def check_segment(value: str) -> Segment:
    if value in SEGMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEGMENT_VALUES!r}")
