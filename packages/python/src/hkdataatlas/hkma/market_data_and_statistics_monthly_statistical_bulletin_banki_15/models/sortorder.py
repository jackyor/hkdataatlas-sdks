from typing import Literal

Sortorder = Literal["asc", "desc"]

SORTORDER_VALUES: set[Sortorder] = {
    "asc",
    "desc",
}


def check_sortorder(value: str) -> Sortorder:
    if value in SORTORDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SORTORDER_VALUES!r}")
