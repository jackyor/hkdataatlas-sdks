from typing import Literal

VacancyRecordCategory = Literal["DAILY", "HOURLY", "MONTHLY"]

VACANCY_RECORD_CATEGORY_VALUES: set[VacancyRecordCategory] = {
    "DAILY",
    "HOURLY",
    "MONTHLY",
}


def check_vacancy_record_category(value: str) -> VacancyRecordCategory:
    if value in VACANCY_RECORD_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VACANCY_RECORD_CATEGORY_VALUES!r}"
    )
