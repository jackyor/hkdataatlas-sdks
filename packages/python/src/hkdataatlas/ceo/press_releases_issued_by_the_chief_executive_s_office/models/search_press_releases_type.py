from typing import Literal

SearchPressReleasesType = Literal["press"]

SEARCH_PRESS_RELEASES_TYPE_VALUES: set[SearchPressReleasesType] = {
    "press",
}


def check_search_press_releases_type(value: str) -> SearchPressReleasesType:
    if value in SEARCH_PRESS_RELEASES_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_PRESS_RELEASES_TYPE_VALUES!r}"
    )
