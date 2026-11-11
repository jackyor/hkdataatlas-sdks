from typing import Literal

GetMapPresentationStyleLang = Literal["en", "sc", "tc"]

GET_MAP_PRESENTATION_STYLE_LANG_VALUES: set[GetMapPresentationStyleLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_map_presentation_style_lang(value: str) -> GetMapPresentationStyleLang:
    if value in GET_MAP_PRESENTATION_STYLE_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MAP_PRESENTATION_STYLE_LANG_VALUES!r}"
    )
