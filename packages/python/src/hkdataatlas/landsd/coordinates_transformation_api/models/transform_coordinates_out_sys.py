from typing import Literal

TransformCoordinatesOutSys = Literal[
    "all", "hkgeog", "hkgrid", "utmgrid", "utmref", "wgsgeog"
]

TRANSFORM_COORDINATES_OUT_SYS_VALUES: set[TransformCoordinatesOutSys] = {
    "all",
    "hkgeog",
    "hkgrid",
    "utmgrid",
    "utmref",
    "wgsgeog",
}


def check_transform_coordinates_out_sys(value: str) -> TransformCoordinatesOutSys:
    if value in TRANSFORM_COORDINATES_OUT_SYS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSFORM_COORDINATES_OUT_SYS_VALUES!r}"
    )
