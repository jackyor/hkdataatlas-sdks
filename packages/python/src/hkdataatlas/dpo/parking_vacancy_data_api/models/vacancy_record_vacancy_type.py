from typing import Literal

VacancyRecordVacancyType = Literal["A", "B", "C"]

VACANCY_RECORD_VACANCY_TYPE_VALUES: set[VacancyRecordVacancyType] = {
    "A",
    "B",
    "C",
}


def check_vacancy_record_vacancy_type(value: str) -> VacancyRecordVacancyType:
    if value in VACANCY_RECORD_VACANCY_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VACANCY_RECORD_VACANCY_TYPE_VALUES!r}"
    )
