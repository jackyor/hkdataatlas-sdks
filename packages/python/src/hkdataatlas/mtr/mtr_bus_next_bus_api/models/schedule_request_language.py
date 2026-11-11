from typing import Literal

ScheduleRequestLanguage = Literal["en", "zh"]

SCHEDULE_REQUEST_LANGUAGE_VALUES: set[ScheduleRequestLanguage] = {
    "en",
    "zh",
}


def check_schedule_request_language(value: str) -> ScheduleRequestLanguage:
    if value in SCHEDULE_REQUEST_LANGUAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEDULE_REQUEST_LANGUAGE_VALUES!r}"
    )
