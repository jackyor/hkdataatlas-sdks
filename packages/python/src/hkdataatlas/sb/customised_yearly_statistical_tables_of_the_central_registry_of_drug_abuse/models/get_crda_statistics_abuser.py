from typing import Literal

GetCrdaStatisticsAbuser = Literal["00000", "00001", "00002"]

GET_CRDA_STATISTICS_ABUSER_VALUES: set[GetCrdaStatisticsAbuser] = {
    "00000",
    "00001",
    "00002",
}


def check_get_crda_statistics_abuser(value: str) -> GetCrdaStatisticsAbuser:
    if value in GET_CRDA_STATISTICS_ABUSER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CRDA_STATISTICS_ABUSER_VALUES!r}"
    )
