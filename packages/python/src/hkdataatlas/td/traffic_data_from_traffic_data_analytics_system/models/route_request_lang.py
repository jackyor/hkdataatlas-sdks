from typing import Literal

RouteRequestLang = Literal["en", "sc", "tc"]

ROUTE_REQUEST_LANG_VALUES: set[RouteRequestLang] = {
    "en",
    "sc",
    "tc",
}


def check_route_request_lang(value: str) -> RouteRequestLang:
    if value in ROUTE_REQUEST_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTE_REQUEST_LANG_VALUES!r}"
    )
