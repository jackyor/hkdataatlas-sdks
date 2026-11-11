from typing import Literal

Searchtype = Literal["chiName", "engName", "regNo"]

SEARCHTYPE_VALUES: set[Searchtype] = {
    "chiName",
    "engName",
    "regNo",
}


def check_searchtype(value: str) -> Searchtype:
    if value in SEARCHTYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCHTYPE_VALUES!r}"
    )
