from typing import Literal

GetFareTableRouteId = Literal[1, 2, 3, 4]

GET_FARE_TABLE_ROUTE_ID_VALUES: set[GetFareTableRouteId] = {
    1,
    2,
    3,
    4,
}


def check_get_fare_table_route_id(value: int) -> GetFareTableRouteId:
    if value in GET_FARE_TABLE_ROUTE_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FARE_TABLE_ROUTE_ID_VALUES!r}"
    )
