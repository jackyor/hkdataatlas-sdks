from typing import Literal

SearchPressReleasesOfficial = Literal[
    "CE",
    "CS",
    "FS",
    "SCED",
    "SCMA",
    "SCS",
    "SCST",
    "SDEV",
    "SED",
    "SEE",
    "SFST",
    "SH",
    "SHH",
    "SHYA",
    "SITI",
    "SJ",
    "SLW",
    "SS",
    "STL",
]

SEARCH_PRESS_RELEASES_OFFICIAL_VALUES: set[SearchPressReleasesOfficial] = {
    "CE",
    "CS",
    "FS",
    "SCED",
    "SCMA",
    "SCS",
    "SCST",
    "SDEV",
    "SED",
    "SEE",
    "SFST",
    "SH",
    "SHH",
    "SHYA",
    "SITI",
    "SJ",
    "SLW",
    "SS",
    "STL",
}


def check_search_press_releases_official(value: str) -> SearchPressReleasesOfficial:
    if value in SEARCH_PRESS_RELEASES_OFFICIAL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_PRESS_RELEASES_OFFICIAL_VALUES!r}"
    )
