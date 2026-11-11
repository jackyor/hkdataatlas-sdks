from typing import Literal

WmsMapServerGetMapVersion = Literal["1.3.0"]

WMS_MAP_SERVER_GET_MAP_VERSION_VALUES: set[WmsMapServerGetMapVersion] = {
    "1.3.0",
}


def check_wms_map_server_get_map_version(value: str) -> WmsMapServerGetMapVersion:
    if value in WMS_MAP_SERVER_GET_MAP_VERSION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WMS_MAP_SERVER_GET_MAP_VERSION_VALUES!r}"
    )
