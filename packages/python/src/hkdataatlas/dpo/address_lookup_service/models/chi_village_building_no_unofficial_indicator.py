from typing import Literal

ChiVillageBuildingNoUnofficialIndicator = Literal["1", "2"]

CHI_VILLAGE_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES: set[
    ChiVillageBuildingNoUnofficialIndicator
] = {
    "1",
    "2",
}


def check_chi_village_building_no_unofficial_indicator(
    value: str,
) -> ChiVillageBuildingNoUnofficialIndicator:
    if value in CHI_VILLAGE_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHI_VILLAGE_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES!r}"
    )
