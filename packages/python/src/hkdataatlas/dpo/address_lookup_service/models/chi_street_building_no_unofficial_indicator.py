from typing import Literal

ChiStreetBuildingNoUnofficialIndicator = Literal["1", "2"]

CHI_STREET_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES: set[
    ChiStreetBuildingNoUnofficialIndicator
] = {
    "1",
    "2",
}


def check_chi_street_building_no_unofficial_indicator(
    value: str,
) -> ChiStreetBuildingNoUnofficialIndicator:
    if value in CHI_STREET_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHI_STREET_BUILDING_NO_UNOFFICIAL_INDICATOR_VALUES!r}"
    )
