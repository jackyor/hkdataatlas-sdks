from typing import Literal

GetCrdaStatisticsPeriodEarlier = Literal[
    "1986-1990", "1991-1995", "1996-2000", "2001-2005", "2006-2010", "2011-2015"
]

GET_CRDA_STATISTICS_PERIOD_EARLIER_VALUES: set[GetCrdaStatisticsPeriodEarlier] = {
    "1986-1990",
    "1991-1995",
    "1996-2000",
    "2001-2005",
    "2006-2010",
    "2011-2015",
}


def check_get_crda_statistics_period_earlier(
    value: str,
) -> GetCrdaStatisticsPeriodEarlier:
    if value in GET_CRDA_STATISTICS_PERIOD_EARLIER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CRDA_STATISTICS_PERIOD_EARLIER_VALUES!r}"
    )
