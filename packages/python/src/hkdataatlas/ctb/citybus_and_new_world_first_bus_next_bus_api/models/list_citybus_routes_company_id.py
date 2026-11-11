from typing import Literal

ListCitybusRoutesCompanyId = Literal["CTB"]

LIST_CITYBUS_ROUTES_COMPANY_ID_VALUES: set[ListCitybusRoutesCompanyId] = {
    "CTB",
}


def check_list_citybus_routes_company_id(value: str) -> ListCitybusRoutesCompanyId:
    if value in LIST_CITYBUS_ROUTES_COMPANY_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CITYBUS_ROUTES_COMPANY_ID_VALUES!r}"
    )
