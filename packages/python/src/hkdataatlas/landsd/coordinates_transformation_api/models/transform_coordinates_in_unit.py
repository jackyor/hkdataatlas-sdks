from typing import Literal

TransformCoordinatesInUnit = Literal["decDeg", "dms"]

TRANSFORM_COORDINATES_IN_UNIT_VALUES: set[TransformCoordinatesInUnit] = {
    "decDeg",
    "dms",
}


def check_transform_coordinates_in_unit(value: str) -> TransformCoordinatesInUnit:
    if value in TRANSFORM_COORDINATES_IN_UNIT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSFORM_COORDINATES_IN_UNIT_VALUES!r}"
    )
