from typing import Literal

GetCitybusCompanyCompanyId = Literal["CTB"]

GET_CITYBUS_COMPANY_COMPANY_ID_VALUES: set[GetCitybusCompanyCompanyId] = {
    "CTB",
}


def check_get_citybus_company_company_id(value: str) -> GetCitybusCompanyCompanyId:
    if value in GET_CITYBUS_COMPANY_COMPANY_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CITYBUS_COMPANY_COMPANY_ID_VALUES!r}"
    )
