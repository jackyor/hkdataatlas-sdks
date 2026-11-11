from typing import Literal

WfsMapServerGetFeatureVersion = Literal["2.0.0"]

WFS_MAP_SERVER_GET_FEATURE_VERSION_VALUES: set[WfsMapServerGetFeatureVersion] = {
    "2.0.0",
}


def check_wfs_map_server_get_feature_version(
    value: str,
) -> WfsMapServerGetFeatureVersion:
    if value in WFS_MAP_SERVER_GET_FEATURE_VERSION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WFS_MAP_SERVER_GET_FEATURE_VERSION_VALUES!r}"
    )
