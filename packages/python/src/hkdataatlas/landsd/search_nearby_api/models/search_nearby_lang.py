from typing import Literal

SearchNearbyLang = Literal["en", "zh"]

SEARCH_NEARBY_LANG_VALUES: set[SearchNearbyLang] = {
    "en",
    "zh",
}


def check_search_nearby_lang(value: str) -> SearchNearbyLang:
    if value in SEARCH_NEARBY_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_NEARBY_LANG_VALUES!r}"
    )
