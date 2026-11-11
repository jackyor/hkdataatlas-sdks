from typing import Literal

ChiStreetBuildingNoConfirmationCode = Literal["A", "B", "C", "P", "X"]

CHI_STREET_BUILDING_NO_CONFIRMATION_CODE_VALUES: set[
    ChiStreetBuildingNoConfirmationCode
] = {
    "A",
    "B",
    "C",
    "P",
    "X",
}


def check_chi_street_building_no_confirmation_code(
    value: str,
) -> ChiStreetBuildingNoConfirmationCode:
    if value in CHI_STREET_BUILDING_NO_CONFIRMATION_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHI_STREET_BUILDING_NO_CONFIRMATION_CODE_VALUES!r}"
    )
