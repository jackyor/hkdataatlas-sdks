from typing import Literal

FindNearbyVehiclesUnit = Literal["ft", "km", "m", "mi"]

FIND_NEARBY_VEHICLES_UNIT_VALUES: set[FindNearbyVehiclesUnit] = {
    "ft",
    "km",
    "m",
    "mi",
}


def check_find_nearby_vehicles_unit(value: str) -> FindNearbyVehiclesUnit:
    if value in FIND_NEARBY_VEHICLES_UNIT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FIND_NEARBY_VEHICLES_UNIT_VALUES!r}"
    )
