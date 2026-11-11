from typing import Literal

GetCitybusEtaCompanyId = Literal["CTB"]

GET_CITYBUS_ETA_COMPANY_ID_VALUES: set[GetCitybusEtaCompanyId] = {
    "CTB",
}


def check_get_citybus_eta_company_id(value: str) -> GetCitybusEtaCompanyId:
    if value in GET_CITYBUS_ETA_COMPANY_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CITYBUS_ETA_COMPANY_ID_VALUES!r}"
    )
