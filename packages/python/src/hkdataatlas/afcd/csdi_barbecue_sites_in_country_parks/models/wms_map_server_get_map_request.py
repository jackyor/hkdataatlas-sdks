from typing import Literal

WmsMapServerGetMapRequest = Literal["GetMap"]

WMS_MAP_SERVER_GET_MAP_REQUEST_VALUES: set[WmsMapServerGetMapRequest] = {
    "GetMap",
}


def check_wms_map_server_get_map_request(value: str) -> WmsMapServerGetMapRequest:
    if value in WMS_MAP_SERVER_GET_MAP_REQUEST_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WMS_MAP_SERVER_GET_MAP_REQUEST_VALUES!r}"
    )
