from typing import Literal

ChiVillageBuildingNoOddEvenIndicator = Literal["B", "E", "O"]

CHI_VILLAGE_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES: set[
    ChiVillageBuildingNoOddEvenIndicator
] = {
    "B",
    "E",
    "O",
}


def check_chi_village_building_no_odd_even_indicator(
    value: str,
) -> ChiVillageBuildingNoOddEvenIndicator:
    if value in CHI_VILLAGE_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHI_VILLAGE_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES!r}"
    )
