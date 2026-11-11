from typing import Literal

GetGsh202021SaleTransactionsSc = Literal["csv", "json", "xml"]

GET_GSH_202021_SALE_TRANSACTIONS_SC_VALUES: set[GetGsh202021SaleTransactionsSc] = {
    "csv",
    "json",
    "xml",
}


def check_get_gsh_202021_sale_transactions_sc(
    value: str,
) -> GetGsh202021SaleTransactionsSc:
    if value in GET_GSH_202021_SALE_TRANSACTIONS_SC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_202021_SALE_TRANSACTIONS_SC_VALUES!r}"
    )
