from typing import Literal

GetStopRoutesCompanyId = Literal["CTB", "NLB"]

GET_STOP_ROUTES_COMPANY_ID_VALUES: set[GetStopRoutesCompanyId] = {
    "CTB",
    "NLB",
}


def check_get_stop_routes_company_id(value: str) -> GetStopRoutesCompanyId:
    if value in GET_STOP_ROUTES_COMPANY_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_STOP_ROUTES_COMPANY_ID_VALUES!r}"
    )
