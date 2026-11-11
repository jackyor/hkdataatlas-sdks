from typing import Literal

SearchPressReleasesLang = Literal["en", "sc", "tc"]

SEARCH_PRESS_RELEASES_LANG_VALUES: set[SearchPressReleasesLang] = {
    "en",
    "sc",
    "tc",
}


def check_search_press_releases_lang(value: str) -> SearchPressReleasesLang:
    if value in SEARCH_PRESS_RELEASES_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_PRESS_RELEASES_LANG_VALUES!r}"
    )
