from typing import Literal

WmsMapServerGetMapService = Literal["WMS"]

WMS_MAP_SERVER_GET_MAP_SERVICE_VALUES: set[WmsMapServerGetMapService] = {
    "WMS",
}


def check_wms_map_server_get_map_service(value: str) -> WmsMapServerGetMapService:
    if value in WMS_MAP_SERVER_GET_MAP_SERVICE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WMS_MAP_SERVER_GET_MAP_SERVICE_VALUES!r}"
    )
