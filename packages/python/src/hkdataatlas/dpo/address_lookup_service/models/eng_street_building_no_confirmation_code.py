from typing import Literal

EngStreetBuildingNoConfirmationCode = Literal["A", "B", "C", "P", "X"]

ENG_STREET_BUILDING_NO_CONFIRMATION_CODE_VALUES: set[
    EngStreetBuildingNoConfirmationCode
] = {
    "A",
    "B",
    "C",
    "P",
    "X",
}


def check_eng_street_building_no_confirmation_code(
    value: str,
) -> EngStreetBuildingNoConfirmationCode:
    if value in ENG_STREET_BUILDING_NO_CONFIRMATION_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENG_STREET_BUILDING_NO_CONFIRMATION_CODE_VALUES!r}"
    )
