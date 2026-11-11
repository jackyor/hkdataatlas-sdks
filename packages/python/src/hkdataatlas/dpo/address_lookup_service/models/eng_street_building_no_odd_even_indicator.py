from typing import Literal

EngStreetBuildingNoOddEvenIndicator = Literal["B", "E", "O"]

ENG_STREET_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES: set[
    EngStreetBuildingNoOddEvenIndicator
] = {
    "B",
    "E",
    "O",
}


def check_eng_street_building_no_odd_even_indicator(
    value: str,
) -> EngStreetBuildingNoOddEvenIndicator:
    if value in ENG_STREET_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENG_STREET_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES!r}"
    )
