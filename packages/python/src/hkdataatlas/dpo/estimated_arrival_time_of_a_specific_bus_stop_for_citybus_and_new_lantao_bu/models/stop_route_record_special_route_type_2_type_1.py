from typing import Literal

StopRouteRecordSpecialRouteType2Type1 = Literal[0, 1]

STOP_ROUTE_RECORD_SPECIAL_ROUTE_TYPE_2_TYPE_1_VALUES: set[
    StopRouteRecordSpecialRouteType2Type1
] = {
    0,
    1,
}


def check_stop_route_record_special_route_type_2_type_1(
    value: int,
) -> StopRouteRecordSpecialRouteType2Type1:
    if value in STOP_ROUTE_RECORD_SPECIAL_ROUTE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ROUTE_RECORD_SPECIAL_ROUTE_TYPE_2_TYPE_1_VALUES!r}"
    )
