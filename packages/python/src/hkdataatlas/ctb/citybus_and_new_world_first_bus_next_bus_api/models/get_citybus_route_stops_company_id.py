from typing import Literal

GetCitybusRouteStopsCompanyId = Literal["CTB"]

GET_CITYBUS_ROUTE_STOPS_COMPANY_ID_VALUES: set[GetCitybusRouteStopsCompanyId] = {
    "CTB",
}


def check_get_citybus_route_stops_company_id(
    value: str,
) -> GetCitybusRouteStopsCompanyId:
    if value in GET_CITYBUS_ROUTE_STOPS_COMPANY_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CITYBUS_ROUTE_STOPS_COMPANY_ID_VALUES!r}"
    )
