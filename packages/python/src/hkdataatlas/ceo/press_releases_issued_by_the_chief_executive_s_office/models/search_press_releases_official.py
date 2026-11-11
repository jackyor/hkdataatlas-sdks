from typing import Literal

SearchPressReleasesOfficial = Literal["CE"]

SEARCH_PRESS_RELEASES_OFFICIAL_VALUES: set[SearchPressReleasesOfficial] = {
    "CE",
}


def check_search_press_releases_official(value: str) -> SearchPressReleasesOfficial:
    if value in SEARCH_PRESS_RELEASES_OFFICIAL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_PRESS_RELEASES_OFFICIAL_VALUES!r}"
    )
