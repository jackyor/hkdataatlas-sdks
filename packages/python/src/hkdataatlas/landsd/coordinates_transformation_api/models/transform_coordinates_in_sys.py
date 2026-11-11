from typing import Literal

TransformCoordinatesInSys = Literal["hkgeog", "hkgrid", "utmgrid", "utmref", "wgsgeog"]

TRANSFORM_COORDINATES_IN_SYS_VALUES: set[TransformCoordinatesInSys] = {
    "hkgeog",
    "hkgrid",
    "utmgrid",
    "utmref",
    "wgsgeog",
}


def check_transform_coordinates_in_sys(value: str) -> TransformCoordinatesInSys:
    if value in TRANSFORM_COORDINATES_IN_SYS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSFORM_COORDINATES_IN_SYS_VALUES!r}"
    )
