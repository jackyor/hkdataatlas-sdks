from typing import Literal

EngVillageBuildingNoConfirmationCode = Literal["A", "B", "C", "P", "X"]

ENG_VILLAGE_BUILDING_NO_CONFIRMATION_CODE_VALUES: set[
    EngVillageBuildingNoConfirmationCode
] = {
    "A",
    "B",
    "C",
    "P",
    "X",
}


def check_eng_village_building_no_confirmation_code(
    value: str,
) -> EngVillageBuildingNoConfirmationCode:
    if value in ENG_VILLAGE_BUILDING_NO_CONFIRMATION_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENG_VILLAGE_BUILDING_NO_CONFIRMATION_CODE_VALUES!r}"
    )
