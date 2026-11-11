from typing import Literal

StopRouteRecordDirType1 = Literal["I", "O"]

STOP_ROUTE_RECORD_DIR_TYPE_1_VALUES: set[StopRouteRecordDirType1] = {
    "I",
    "O",
}


def check_stop_route_record_dir_type_1(value: str) -> StopRouteRecordDirType1:
    if value in STOP_ROUTE_RECORD_DIR_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ROUTE_RECORD_DIR_TYPE_1_VALUES!r}"
    )
