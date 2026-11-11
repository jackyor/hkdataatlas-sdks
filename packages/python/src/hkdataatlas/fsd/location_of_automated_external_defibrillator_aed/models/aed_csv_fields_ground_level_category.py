from typing import Literal

AedCsvFieldsGroundLevelCategory = Literal["Non-Street Level", "Street Level"]

AED_CSV_FIELDS_GROUND_LEVEL_CATEGORY_VALUES: set[AedCsvFieldsGroundLevelCategory] = {
    "Non-Street Level",
    "Street Level",
}


def check_aed_csv_fields_ground_level_category(
    value: str,
) -> AedCsvFieldsGroundLevelCategory:
    if value in AED_CSV_FIELDS_GROUND_LEVEL_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AED_CSV_FIELDS_GROUND_LEVEL_CATEGORY_VALUES!r}"
    )
