from typing import Literal

ChiVillageBuildingNoConfirmationCode = Literal["A", "B", "C", "P", "X"]

CHI_VILLAGE_BUILDING_NO_CONFIRMATION_CODE_VALUES: set[
    ChiVillageBuildingNoConfirmationCode
] = {
    "A",
    "B",
    "C",
    "P",
    "X",
}


def check_chi_village_building_no_confirmation_code(
    value: str,
) -> ChiVillageBuildingNoConfirmationCode:
    if value in CHI_VILLAGE_BUILDING_NO_CONFIRMATION_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHI_VILLAGE_BUILDING_NO_CONFIRMATION_CODE_VALUES!r}"
    )
