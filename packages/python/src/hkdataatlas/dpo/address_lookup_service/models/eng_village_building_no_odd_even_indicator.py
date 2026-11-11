from typing import Literal

EngVillageBuildingNoOddEvenIndicator = Literal["B", "E", "O"]

ENG_VILLAGE_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES: set[
    EngVillageBuildingNoOddEvenIndicator
] = {
    "B",
    "E",
    "O",
}


def check_eng_village_building_no_odd_even_indicator(
    value: str,
) -> EngVillageBuildingNoOddEvenIndicator:
    if value in ENG_VILLAGE_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENG_VILLAGE_BUILDING_NO_ODD_EVEN_INDICATOR_VALUES!r}"
    )
