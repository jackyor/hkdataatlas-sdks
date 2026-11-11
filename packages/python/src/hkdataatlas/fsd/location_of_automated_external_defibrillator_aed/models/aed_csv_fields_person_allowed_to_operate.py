from typing import Literal

AedCsvFieldsPersonAllowedToOperate = Literal[
    "Anyone", "Staff Only", "Trained Personnel Only", "Trained Staff Only"
]

AED_CSV_FIELDS_PERSON_ALLOWED_TO_OPERATE_VALUES: set[
    AedCsvFieldsPersonAllowedToOperate
] = {
    "Anyone",
    "Staff Only",
    "Trained Personnel Only",
    "Trained Staff Only",
}


def check_aed_csv_fields_person_allowed_to_operate(
    value: str,
) -> AedCsvFieldsPersonAllowedToOperate:
    if value in AED_CSV_FIELDS_PERSON_ALLOWED_TO_OPERATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AED_CSV_FIELDS_PERSON_ALLOWED_TO_OPERATE_VALUES!r}"
    )
