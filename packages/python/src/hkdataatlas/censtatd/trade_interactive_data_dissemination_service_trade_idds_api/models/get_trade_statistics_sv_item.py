from typing import Literal

GetTradeStatisticsSvItem = Literal["QCm", "QCy", "VCm", "VCy"]

GET_TRADE_STATISTICS_SV_ITEM_VALUES: set[GetTradeStatisticsSvItem] = {
    "QCm",
    "QCy",
    "VCm",
    "VCy",
}


def check_get_trade_statistics_sv_item(value: str) -> GetTradeStatisticsSvItem:
    if value in GET_TRADE_STATISTICS_SV_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TRADE_STATISTICS_SV_ITEM_VALUES!r}"
    )
