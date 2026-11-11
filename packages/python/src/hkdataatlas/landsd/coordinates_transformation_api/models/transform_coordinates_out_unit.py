from typing import Literal

TransformCoordinatesOutUnit = Literal["decDeg", "decMin", "dms"]

TRANSFORM_COORDINATES_OUT_UNIT_VALUES: set[TransformCoordinatesOutUnit] = {
    "decDeg",
    "decMin",
    "dms",
}


def check_transform_coordinates_out_unit(value: str) -> TransformCoordinatesOutUnit:
    if value in TRANSFORM_COORDINATES_OUT_UNIT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSFORM_COORDINATES_OUT_UNIT_VALUES!r}"
    )
