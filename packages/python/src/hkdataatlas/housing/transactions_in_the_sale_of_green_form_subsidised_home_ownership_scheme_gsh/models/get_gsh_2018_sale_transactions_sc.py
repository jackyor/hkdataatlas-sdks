from typing import Literal

GetGsh2018SaleTransactionsSc = Literal["csv", "json", "xml"]

GET_GSH_2018_SALE_TRANSACTIONS_SC_VALUES: set[GetGsh2018SaleTransactionsSc] = {
    "csv",
    "json",
    "xml",
}


def check_get_gsh_2018_sale_transactions_sc(value: str) -> GetGsh2018SaleTransactionsSc:
    if value in GET_GSH_2018_SALE_TRANSACTIONS_SC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2018_SALE_TRANSACTIONS_SC_VALUES!r}"
    )
