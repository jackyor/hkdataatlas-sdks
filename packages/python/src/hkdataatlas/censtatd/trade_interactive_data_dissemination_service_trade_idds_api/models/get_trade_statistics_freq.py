from typing import Literal

GetTradeStatisticsFreq = Literal["A", "M"]

GET_TRADE_STATISTICS_FREQ_VALUES: set[GetTradeStatisticsFreq] = {
    "A",
    "M",
}


def check_get_trade_statistics_freq(value: str) -> GetTradeStatisticsFreq:
    if value in GET_TRADE_STATISTICS_FREQ_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TRADE_STATISTICS_FREQ_VALUES!r}"
    )
