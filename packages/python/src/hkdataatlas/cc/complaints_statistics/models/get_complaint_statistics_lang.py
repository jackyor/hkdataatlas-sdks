from typing import Literal

GetComplaintStatisticsLang = Literal["en", "sc", "tc"]

GET_COMPLAINT_STATISTICS_LANG_VALUES: set[GetComplaintStatisticsLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_complaint_statistics_lang(value: str) -> GetComplaintStatisticsLang:
    if value in GET_COMPLAINT_STATISTICS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_COMPLAINT_STATISTICS_LANG_VALUES!r}"
    )
