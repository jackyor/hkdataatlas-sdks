from typing import Literal

GetVectorMapLabelTileLang = Literal["en", "sc", "tc"]

GET_VECTOR_MAP_LABEL_TILE_LANG_VALUES: set[GetVectorMapLabelTileLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_vector_map_label_tile_lang(value: str) -> GetVectorMapLabelTileLang:
    if value in GET_VECTOR_MAP_LABEL_TILE_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_VECTOR_MAP_LABEL_TILE_LANG_VALUES!r}"
    )
