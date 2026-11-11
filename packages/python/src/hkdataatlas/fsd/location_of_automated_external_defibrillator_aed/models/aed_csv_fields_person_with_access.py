from typing import Literal

AedCsvFieldsPersonWithAccess = Literal[
    "Accompanied By Staff Only",
    "Anyone",
    "Staff Only",
    "Teaching And Non-Teaching Staff",
    "Trained Staff Only",
]

AED_CSV_FIELDS_PERSON_WITH_ACCESS_VALUES: set[AedCsvFieldsPersonWithAccess] = {
    "Accompanied By Staff Only",
    "Anyone",
    "Staff Only",
    "Teaching And Non-Teaching Staff",
    "Trained Staff Only",
}


def check_aed_csv_fields_person_with_access(value: str) -> AedCsvFieldsPersonWithAccess:
    if value in AED_CSV_FIELDS_PERSON_WITH_ACCESS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AED_CSV_FIELDS_PERSON_WITH_ACCESS_VALUES!r}"
    )
