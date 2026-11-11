from typing import Literal

GetHos2018SaleTransactionsSc = Literal["csv", "json", "xml"]

GET_HOS_2018_SALE_TRANSACTIONS_SC_VALUES: set[GetHos2018SaleTransactionsSc] = {
    "csv",
    "json",
    "xml",
}


def check_get_hos_2018_sale_transactions_sc(value: str) -> GetHos2018SaleTransactionsSc:
    if value in GET_HOS_2018_SALE_TRANSACTIONS_SC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2018_SALE_TRANSACTIONS_SC_VALUES!r}"
    )
