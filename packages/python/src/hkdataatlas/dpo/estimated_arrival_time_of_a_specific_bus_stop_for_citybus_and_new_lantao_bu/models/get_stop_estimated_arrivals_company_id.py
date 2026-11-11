from typing import Literal

GetStopEstimatedArrivalsCompanyId = Literal["CTB", "NLB"]

GET_STOP_ESTIMATED_ARRIVALS_COMPANY_ID_VALUES: set[
    GetStopEstimatedArrivalsCompanyId
] = {
    "CTB",
    "NLB",
}


def check_get_stop_estimated_arrivals_company_id(
    value: str,
) -> GetStopEstimatedArrivalsCompanyId:
    if value in GET_STOP_ESTIMATED_ARRIVALS_COMPANY_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_STOP_ESTIMATED_ARRIVALS_COMPANY_ID_VALUES!r}"
    )
