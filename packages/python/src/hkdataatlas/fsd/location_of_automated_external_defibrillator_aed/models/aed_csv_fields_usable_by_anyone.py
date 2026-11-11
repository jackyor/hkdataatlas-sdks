from typing import Literal

AedCsvFieldsUsableByAnyone = Literal["No", "Yes"]

AED_CSV_FIELDS_USABLE_BY_ANYONE_VALUES: set[AedCsvFieldsUsableByAnyone] = {
    "No",
    "Yes",
}


def check_aed_csv_fields_usable_by_anyone(value: str) -> AedCsvFieldsUsableByAnyone:
    if value in AED_CSV_FIELDS_USABLE_BY_ANYONE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AED_CSV_FIELDS_USABLE_BY_ANYONE_VALUES!r}"
    )
