from typing import Literal

GetTradeStatisticsCodeclass = Literal[
    "EUC",
    "HKHS",
    "HKHS2",
    "HKHS4",
    "HKHS6",
    "HKHS8",
    "SITC",
    "SITC1",
    "SITC2",
    "SITC3",
    "SITC5",
]

GET_TRADE_STATISTICS_CODECLASS_VALUES: set[GetTradeStatisticsCodeclass] = {
    "EUC",
    "HKHS",
    "HKHS2",
    "HKHS4",
    "HKHS6",
    "HKHS8",
    "SITC",
    "SITC1",
    "SITC2",
    "SITC3",
    "SITC5",
}


def check_get_trade_statistics_codeclass(value: str) -> GetTradeStatisticsCodeclass:
    if value in GET_TRADE_STATISTICS_CODECLASS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TRADE_STATISTICS_CODECLASS_VALUES!r}"
    )
