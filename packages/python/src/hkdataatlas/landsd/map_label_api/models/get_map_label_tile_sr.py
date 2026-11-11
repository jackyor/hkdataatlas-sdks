from typing import Literal

GetMapLabelTileSr = Literal["HK80", "WGS84"]

GET_MAP_LABEL_TILE_SR_VALUES: set[GetMapLabelTileSr] = {
    "HK80",
    "WGS84",
}


def check_get_map_label_tile_sr(value: str) -> GetMapLabelTileSr:
    if value in GET_MAP_LABEL_TILE_SR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MAP_LABEL_TILE_SR_VALUES!r}"
    )
