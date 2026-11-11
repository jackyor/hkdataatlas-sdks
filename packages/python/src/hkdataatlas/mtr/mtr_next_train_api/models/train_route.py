from typing import Literal

TrainRoute = Literal["", "RAC"]

TRAIN_ROUTE_VALUES: set[TrainRoute] = {
    "",
    "RAC",
}


def check_train_route(value: str) -> TrainRoute:
    if value in TRAIN_ROUTE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRAIN_ROUTE_VALUES!r}"
    )
