from typing import Literal

GetTimetableRouteId = Literal[1, 2, 3, 4]

GET_TIMETABLE_ROUTE_ID_VALUES: set[GetTimetableRouteId] = {
    1,
    2,
    3,
    4,
}


def check_get_timetable_route_id(value: int) -> GetTimetableRouteId:
    if value in GET_TIMETABLE_ROUTE_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TIMETABLE_ROUTE_ID_VALUES!r}"
    )
