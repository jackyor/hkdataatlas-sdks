from typing import Literal

GetEtaRouteId = Literal[1, 2, 3, 4]

GET_ETA_ROUTE_ID_VALUES: set[GetEtaRouteId] = {
    1,
    2,
    3,
    4,
}


def check_get_eta_route_id(value: int) -> GetEtaRouteId:
    if value in GET_ETA_ROUTE_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ETA_ROUTE_ID_VALUES!r}"
    )
