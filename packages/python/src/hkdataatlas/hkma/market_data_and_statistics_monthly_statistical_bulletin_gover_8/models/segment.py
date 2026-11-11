from typing import Literal

Segment = Literal[
    "Benchmark", "MaturedPrices", "MaturedYields", "OutstandPrices", "OutstandYields"
]

SEGMENT_VALUES: set[Segment] = {
    "Benchmark",
    "MaturedPrices",
    "MaturedYields",
    "OutstandPrices",
    "OutstandYields",
}


def check_segment(value: str) -> Segment:
    if value in SEGMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEGMENT_VALUES!r}")
