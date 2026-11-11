from typing import Literal

GetHos2022SaleTransactionsSc = Literal["csv", "json", "xml"]

GET_HOS_2022_SALE_TRANSACTIONS_SC_VALUES: set[GetHos2022SaleTransactionsSc] = {
    "csv",
    "json",
    "xml",
}


def check_get_hos_2022_sale_transactions_sc(value: str) -> GetHos2022SaleTransactionsSc:
    if value in GET_HOS_2022_SALE_TRANSACTIONS_SC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2022_SALE_TRANSACTIONS_SC_VALUES!r}"
    )
