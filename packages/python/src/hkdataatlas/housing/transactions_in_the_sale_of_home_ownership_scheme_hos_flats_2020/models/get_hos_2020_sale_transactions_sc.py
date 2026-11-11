from typing import Literal

GetHos2020SaleTransactionsSc = Literal["csv", "json", "xml"]

GET_HOS_2020_SALE_TRANSACTIONS_SC_VALUES: set[GetHos2020SaleTransactionsSc] = {
    "csv",
    "json",
    "xml",
}


def check_get_hos_2020_sale_transactions_sc(value: str) -> GetHos2020SaleTransactionsSc:
    if value in GET_HOS_2020_SALE_TRANSACTIONS_SC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2020_SALE_TRANSACTIONS_SC_VALUES!r}"
    )
