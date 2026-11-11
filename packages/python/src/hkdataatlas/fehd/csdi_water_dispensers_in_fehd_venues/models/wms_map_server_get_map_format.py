from typing import Literal

WmsMapServerGetMapFormat = Literal[
    "image/bmp",
    "image/gif",
    "image/jpeg",
    "image/png",
    "image/png24",
    "image/png32",
    "image/png8",
    "image/svg+xml",
    "image/tiff",
]

WMS_MAP_SERVER_GET_MAP_FORMAT_VALUES: set[WmsMapServerGetMapFormat] = {
    "image/bmp",
    "image/gif",
    "image/jpeg",
    "image/png",
    "image/png24",
    "image/png32",
    "image/png8",
    "image/svg+xml",
    "image/tiff",
}


def check_wms_map_server_get_map_format(value: str) -> WmsMapServerGetMapFormat:
    if value in WMS_MAP_SERVER_GET_MAP_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WMS_MAP_SERVER_GET_MAP_FORMAT_VALUES!r}"
    )
