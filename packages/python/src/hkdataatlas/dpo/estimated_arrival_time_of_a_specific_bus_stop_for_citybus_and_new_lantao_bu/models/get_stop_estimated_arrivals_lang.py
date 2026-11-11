from typing import Literal

GetStopEstimatedArrivalsLang = Literal["en", "zh-hans", "zh-hant"]

GET_STOP_ESTIMATED_ARRIVALS_LANG_VALUES: set[GetStopEstimatedArrivalsLang] = {
    "en",
    "zh-hans",
    "zh-hant",
}


def check_get_stop_estimated_arrivals_lang(value: str) -> GetStopEstimatedArrivalsLang:
    if value in GET_STOP_ESTIMATED_ARRIVALS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_STOP_ESTIMATED_ARRIVALS_LANG_VALUES!r}"
    )
