from typing import Literal

ChiStreetBuildingNoOddEvenIndicator = Literal["B", "E", "O"]

CHI_STREET_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES: set[
    ChiStreetBuildingNoOddEvenIndicator
] = {
    "B",
    "E",
    "O",
}


def check_chi_street_building_no_odd_even_indicator(
    value: str,
) -> ChiStreetBuildingNoOddEvenIndicator:
    if value in CHI_STREET_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHI_STREET_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES!r}"
    )
