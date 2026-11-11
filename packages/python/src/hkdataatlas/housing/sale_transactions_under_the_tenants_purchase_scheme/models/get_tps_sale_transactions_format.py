from typing import Literal

GetTpsSaleTransactionsFormat = Literal["json"]

GET_TPS_SALE_TRANSACTIONS_FORMAT_VALUES: set[GetTpsSaleTransactionsFormat] = {
    "json",
}


def check_get_tps_sale_transactions_format(value: str) -> GetTpsSaleTransactionsFormat:
    if value in GET_TPS_SALE_TRANSACTIONS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TPS_SALE_TRANSACTIONS_FORMAT_VALUES!r}"
    )
