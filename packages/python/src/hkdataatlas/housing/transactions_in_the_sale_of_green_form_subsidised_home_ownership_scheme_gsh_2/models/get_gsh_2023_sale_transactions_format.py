from typing import Literal

GetGsh2023SaleTransactionsFormat = Literal["csv", "json", "xml"]

GET_GSH_2023_SALE_TRANSACTIONS_FORMAT_VALUES: set[GetGsh2023SaleTransactionsFormat] = {
    "csv",
    "json",
    "xml",
}


def check_get_gsh_2023_sale_transactions_format(
    value: str,
) -> GetGsh2023SaleTransactionsFormat:
    if value in GET_GSH_2023_SALE_TRANSACTIONS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2023_SALE_TRANSACTIONS_FORMAT_VALUES!r}"
    )
