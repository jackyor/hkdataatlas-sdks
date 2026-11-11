from typing import Literal

GetCrdaStatisticsPeriod = Literal[
    "2016-2025",
    "2017-2025",
    "2018-2025",
    "2019-2025",
    "2020-2025",
    "2021-2025",
    "2022-2025",
]

GET_CRDA_STATISTICS_PERIOD_VALUES: set[GetCrdaStatisticsPeriod] = {
    "2016-2025",
    "2017-2025",
    "2018-2025",
    "2019-2025",
    "2020-2025",
    "2021-2025",
    "2022-2025",
}


def check_get_crda_statistics_period(value: str) -> GetCrdaStatisticsPeriod:
    if value in GET_CRDA_STATISTICS_PERIOD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CRDA_STATISTICS_PERIOD_VALUES!r}"
    )
