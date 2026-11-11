from typing import Literal

GetImageryMapTileSr = Literal["HK80", "WGS84"]

GET_IMAGERY_MAP_TILE_SR_VALUES: set[GetImageryMapTileSr] = {
    "HK80",
    "WGS84",
}


def check_get_imagery_map_tile_sr(value: str) -> GetImageryMapTileSr:
    if value in GET_IMAGERY_MAP_TILE_SR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_IMAGERY_MAP_TILE_SR_VALUES!r}"
    )
