from typing import Literal

CarparkInfoLang = Literal["en_US", "zh_CN", "zh_TW"]

CARPARK_INFO_LANG_VALUES: set[CarparkInfoLang] = {
    "en_US",
    "zh_CN",
    "zh_TW",
}


def check_carpark_info_lang(value: str) -> CarparkInfoLang:
    if value in CARPARK_INFO_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CARPARK_INFO_LANG_VALUES!r}"
    )
