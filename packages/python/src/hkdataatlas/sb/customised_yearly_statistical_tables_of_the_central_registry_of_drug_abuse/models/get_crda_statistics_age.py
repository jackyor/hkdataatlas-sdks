from typing import Literal

GetCrdaStatisticsAge = Literal[
    "00001", "00002", "00003", "00004", "00005", "00006", "00999"
]

GET_CRDA_STATISTICS_AGE_VALUES: set[GetCrdaStatisticsAge] = {
    "00001",
    "00002",
    "00003",
    "00004",
    "00005",
    "00006",
    "00999",
}


def check_get_crda_statistics_age(value: str) -> GetCrdaStatisticsAge:
    if value in GET_CRDA_STATISTICS_AGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CRDA_STATISTICS_AGE_VALUES!r}"
    )
