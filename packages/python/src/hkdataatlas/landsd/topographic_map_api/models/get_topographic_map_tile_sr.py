from typing import Literal

GetTopographicMapTileSr = Literal["HK80", "WGS84"]

GET_TOPOGRAPHIC_MAP_TILE_SR_VALUES: set[GetTopographicMapTileSr] = {
    "HK80",
    "WGS84",
}


def check_get_topographic_map_tile_sr(value: str) -> GetTopographicMapTileSr:
    if value in GET_TOPOGRAPHIC_MAP_TILE_SR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TOPOGRAPHIC_MAP_TILE_SR_VALUES!r}"
    )
