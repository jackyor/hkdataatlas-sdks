from typing import Literal

StopOperationsAction = Literal["estimatedArrivals", "list"]

STOP_OPERATIONS_ACTION_VALUES: set[StopOperationsAction] = {
    "estimatedArrivals",
    "list",
}


def check_stop_operations_action(value: str) -> StopOperationsAction:
    if value in STOP_OPERATIONS_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_OPERATIONS_ACTION_VALUES!r}"
    )
