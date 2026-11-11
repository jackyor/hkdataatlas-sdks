from typing import Literal

GetGsh2019SaleTransactionsFormat = Literal["csv", "json", "xml"]

GET_GSH_2019_SALE_TRANSACTIONS_FORMAT_VALUES: set[GetGsh2019SaleTransactionsFormat] = {
    "csv",
    "json",
    "xml",
}


def check_get_gsh_2019_sale_transactions_format(
    value: str,
) -> GetGsh2019SaleTransactionsFormat:
    if value in GET_GSH_2019_SALE_TRANSACTIONS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2019_SALE_TRANSACTIONS_FORMAT_VALUES!r}"
    )
