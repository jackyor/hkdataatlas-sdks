from typing import Literal

GetCitybusRouteCompanyId = Literal["CTB"]

GET_CITYBUS_ROUTE_COMPANY_ID_VALUES: set[GetCitybusRouteCompanyId] = {
    "CTB",
}


def check_get_citybus_route_company_id(value: str) -> GetCitybusRouteCompanyId:
    if value in GET_CITYBUS_ROUTE_COMPANY_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CITYBUS_ROUTE_COMPANY_ID_VALUES!r}"
    )
