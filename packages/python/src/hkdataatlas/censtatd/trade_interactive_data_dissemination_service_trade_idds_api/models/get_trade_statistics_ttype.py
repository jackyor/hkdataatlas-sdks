from typing import Literal

GetTradeStatisticsTtype = Literal["1", "2", "3", "4", "5", "ALL"]

GET_TRADE_STATISTICS_TTYPE_VALUES: set[GetTradeStatisticsTtype] = {
    "1",
    "2",
    "3",
    "4",
    "5",
    "ALL",
}


def check_get_trade_statistics_ttype(value: str) -> GetTradeStatisticsTtype:
    if value in GET_TRADE_STATISTICS_TTYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TRADE_STATISTICS_TTYPE_VALUES!r}"
    )
