from typing import Literal

GetStopRoutesLang = Literal["en", "zh-hans", "zh-hant"]

GET_STOP_ROUTES_LANG_VALUES: set[GetStopRoutesLang] = {
    "en",
    "zh-hans",
    "zh-hant",
}


def check_get_stop_routes_lang(value: str) -> GetStopRoutesLang:
    if value in GET_STOP_ROUTES_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_STOP_ROUTES_LANG_VALUES!r}"
    )
