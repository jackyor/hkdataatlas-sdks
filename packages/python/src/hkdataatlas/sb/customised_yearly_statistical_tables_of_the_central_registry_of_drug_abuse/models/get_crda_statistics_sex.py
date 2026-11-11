from typing import Literal

GetCrdaStatisticsSex = Literal["00001", "00002", "00999"]

GET_CRDA_STATISTICS_SEX_VALUES: set[GetCrdaStatisticsSex] = {
    "00001",
    "00002",
    "00999",
}


def check_get_crda_statistics_sex(value: str) -> GetCrdaStatisticsSex:
    if value in GET_CRDA_STATISTICS_SEX_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CRDA_STATISTICS_SEX_VALUES!r}"
    )
