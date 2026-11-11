from typing import Literal

GetVectorMapTileSr = Literal["HK80", "WGS84"]

GET_VECTOR_MAP_TILE_SR_VALUES: set[GetVectorMapTileSr] = {
    "HK80",
    "WGS84",
}


def check_get_vector_map_tile_sr(value: str) -> GetVectorMapTileSr:
    if value in GET_VECTOR_MAP_TILE_SR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_VECTOR_MAP_TILE_SR_VALUES!r}"
    )
