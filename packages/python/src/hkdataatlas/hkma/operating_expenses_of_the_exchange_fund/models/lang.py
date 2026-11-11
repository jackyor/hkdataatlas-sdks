from typing import Literal

Lang = Literal["en"]

LANG_VALUES: set[Lang] = {
    "en",
}


def check_lang(value: str) -> Lang:
    if value in LANG_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LANG_VALUES!r}")
