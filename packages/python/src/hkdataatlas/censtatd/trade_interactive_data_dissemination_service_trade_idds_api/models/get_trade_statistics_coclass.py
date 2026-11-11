from typing import Literal

GetTradeStatisticsCoclass = Literal["C", "R"]

GET_TRADE_STATISTICS_COCLASS_VALUES: set[GetTradeStatisticsCoclass] = {
    "C",
    "R",
}


def check_get_trade_statistics_coclass(value: str) -> GetTradeStatisticsCoclass:
    if value in GET_TRADE_STATISTICS_COCLASS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TRADE_STATISTICS_COCLASS_VALUES!r}"
    )
