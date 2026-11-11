from typing import Literal

EngStreetBuildingNoUnofficialIndicator = Literal["1", "2"]

ENG_STREET_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES: set[
    EngStreetBuildingNoUnofficialIndicator
] = {
    "1",
    "2",
}


def check_eng_street_building_no_unofficial_indicator(
    value: str,
) -> EngStreetBuildingNoUnofficialIndicator:
    if value in ENG_STREET_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENG_STREET_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES!r}"
    )
