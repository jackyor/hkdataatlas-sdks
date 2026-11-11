from typing import Literal

GetTradeStatisticsLang = Literal["EN", "SC", "TC"]

GET_TRADE_STATISTICS_LANG_VALUES: set[GetTradeStatisticsLang] = {
    "EN",
    "SC",
    "TC",
}


def check_get_trade_statistics_lang(value: str) -> GetTradeStatisticsLang:
    if value in GET_TRADE_STATISTICS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TRADE_STATISTICS_LANG_VALUES!r}"
    )
