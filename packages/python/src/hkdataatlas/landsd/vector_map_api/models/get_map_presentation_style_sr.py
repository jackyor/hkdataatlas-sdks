from typing import Literal

GetMapPresentationStyleSr = Literal["HK80", "WGS84"]

GET_MAP_PRESENTATION_STYLE_SR_VALUES: set[GetMapPresentationStyleSr] = {
    "HK80",
    "WGS84",
}


def check_get_map_presentation_style_sr(value: str) -> GetMapPresentationStyleSr:
    if value in GET_MAP_PRESENTATION_STYLE_SR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MAP_PRESENTATION_STYLE_SR_VALUES!r}"
    )
