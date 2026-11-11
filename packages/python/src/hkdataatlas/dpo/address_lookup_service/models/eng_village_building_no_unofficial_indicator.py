from typing import Literal

EngVillageBuildingNoUnofficialIndicator = Literal["1", "2"]

ENG_VILLAGE_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES: set[
    EngVillageBuildingNoUnofficialIndicator
] = {
    "1",
    "2",
}


def check_eng_village_building_no_unofficial_indicator(
    value: str,
) -> EngVillageBuildingNoUnofficialIndicator:
    if value in ENG_VILLAGE_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENG_VILLAGE_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES!r}"
    )
