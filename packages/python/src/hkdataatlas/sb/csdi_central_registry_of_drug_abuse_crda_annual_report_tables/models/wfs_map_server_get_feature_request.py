from typing import Literal

WfsMapServerGetFeatureRequest = Literal["GetFeature"]

WFS_MAP_SERVER_GET_FEATURE_REQUEST_VALUES: set[WfsMapServerGetFeatureRequest] = {
    "GetFeature",
}


def check_wfs_map_server_get_feature_request(
    value: str,
) -> WfsMapServerGetFeatureRequest:
    if value in WFS_MAP_SERVER_GET_FEATURE_REQUEST_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WFS_MAP_SERVER_GET_FEATURE_REQUEST_VALUES!r}"
    )
