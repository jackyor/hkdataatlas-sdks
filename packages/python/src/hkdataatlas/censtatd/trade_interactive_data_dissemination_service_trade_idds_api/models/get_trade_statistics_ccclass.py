from typing import Literal

GetTradeStatisticsCcclass = Literal["C", "R"]

GET_TRADE_STATISTICS_CCCLASS_VALUES: set[GetTradeStatisticsCcclass] = {
    "C",
    "R",
}


def check_get_trade_statistics_ccclass(value: str) -> GetTradeStatisticsCcclass:
    if value in GET_TRADE_STATISTICS_CCCLASS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TRADE_STATISTICS_CCCLASS_VALUES!r}"
    )
