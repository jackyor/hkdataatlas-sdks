from typing import Literal

GetVectorMapLabelTileSr = Literal["HK80", "WGS84"]

GET_VECTOR_MAP_LABEL_TILE_SR_VALUES: set[GetVectorMapLabelTileSr] = {
    "HK80",
    "WGS84",
}


def check_get_vector_map_label_tile_sr(value: str) -> GetVectorMapLabelTileSr:
    if value in GET_VECTOR_MAP_LABEL_TILE_SR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_VECTOR_MAP_LABEL_TILE_SR_VALUES!r}"
    )
