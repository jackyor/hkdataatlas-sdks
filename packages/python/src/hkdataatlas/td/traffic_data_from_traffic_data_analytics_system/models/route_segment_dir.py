from typing import Literal

RouteSegmentDir = Literal[0, 1, 2, 3, 4]

ROUTE_SEGMENT_DIR_VALUES: set[RouteSegmentDir] = {
    0,
    1,
    2,
    3,
    4,
}


def check_route_segment_dir(value: int) -> RouteSegmentDir:
    if value in ROUTE_SEGMENT_DIR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_SEGMENT_DIR_VALUES!r}"
    )
