from typing import Literal

StopRouteRecordOvernightRouteType3Type1 = Literal[0, 1]

STOP_ROUTE_RECORD_OVERNIGHT_ROUTE_TYPE_3_TYPE_1_VALUES: set[
    StopRouteRecordOvernightRouteType3Type1
] = {
    0,
    1,
}


def check_stop_route_record_overnight_route_type_3_type_1(
    value: int,
) -> StopRouteRecordOvernightRouteType3Type1:
    if value in STOP_ROUTE_RECORD_OVERNIGHT_ROUTE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ROUTE_RECORD_OVERNIGHT_ROUTE_TYPE_3_TYPE_1_VALUES!r}"
    )
