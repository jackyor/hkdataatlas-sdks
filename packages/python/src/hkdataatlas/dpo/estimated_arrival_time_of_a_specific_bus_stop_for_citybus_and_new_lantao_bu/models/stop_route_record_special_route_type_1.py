from typing import Literal

StopRouteRecordSpecialRouteType1 = Literal[0, 1]

STOP_ROUTE_RECORD_SPECIAL_ROUTE_TYPE_1_VALUES: set[StopRouteRecordSpecialRouteType1] = {
    0,
    1,
}


def check_stop_route_record_special_route_type_1(
    value: int,
) -> StopRouteRecordSpecialRouteType1:
    if value in STOP_ROUTE_RECORD_SPECIAL_ROUTE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ROUTE_RECORD_SPECIAL_ROUTE_TYPE_1_VALUES!r}"
    )
