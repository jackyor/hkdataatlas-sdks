from typing import Literal

WfsMapServerGetFeatureService = Literal["WFS"]

WFS_MAP_SERVER_GET_FEATURE_SERVICE_VALUES: set[WfsMapServerGetFeatureService] = {
    "WFS",
}


def check_wfs_map_server_get_feature_service(
    value: str,
) -> WfsMapServerGetFeatureService:
    if value in WFS_MAP_SERVER_GET_FEATURE_SERVICE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WFS_MAP_SERVER_GET_FEATURE_SERVICE_VALUES!r}"
    )
