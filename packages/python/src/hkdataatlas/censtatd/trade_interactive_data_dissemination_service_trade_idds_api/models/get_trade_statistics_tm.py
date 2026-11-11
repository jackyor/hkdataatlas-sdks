from typing import Literal

GetTradeStatisticsTm = Literal["Y"]

GET_TRADE_STATISTICS_TM_VALUES: set[GetTradeStatisticsTm] = {
    "Y",
}


def check_get_trade_statistics_tm(value: str) -> GetTradeStatisticsTm:
    if value in GET_TRADE_STATISTICS_TM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TRADE_STATISTICS_TM_VALUES!r}"
    )
