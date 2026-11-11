from typing import Literal

GetScheduleLang = Literal["EN", "TC"]

GET_SCHEDULE_LANG_VALUES: set[GetScheduleLang] = {
    "EN",
    "TC",
}


def check_get_schedule_lang(value: str) -> GetScheduleLang:
    if value in GET_SCHEDULE_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_SCHEDULE_LANG_VALUES!r}"
    )
