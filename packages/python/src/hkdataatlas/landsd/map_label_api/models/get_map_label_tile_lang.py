from typing import Literal

GetMapLabelTileLang = Literal["en", "sc", "tc"]

GET_MAP_LABEL_TILE_LANG_VALUES: set[GetMapLabelTileLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_map_label_tile_lang(value: str) -> GetMapLabelTileLang:
    if value in GET_MAP_LABEL_TILE_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MAP_LABEL_TILE_LANG_VALUES!r}"
    )
