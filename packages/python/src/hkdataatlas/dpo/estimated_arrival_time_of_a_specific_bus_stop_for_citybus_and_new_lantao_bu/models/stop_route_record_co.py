from typing import Literal

StopRouteRecordCo = Literal["CTB", "NLB"]

STOP_ROUTE_RECORD_CO_VALUES: set[StopRouteRecordCo] = {
    "CTB",
    "NLB",
}


def check_stop_route_record_co(value: str) -> StopRouteRecordCo:
    if value in STOP_ROUTE_RECORD_CO_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ROUTE_RECORD_CO_VALUES!r}"
    )
