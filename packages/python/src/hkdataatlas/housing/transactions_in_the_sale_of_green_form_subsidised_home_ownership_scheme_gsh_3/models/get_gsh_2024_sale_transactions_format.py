from typing import Literal

GetGsh2024SaleTransactionsFormat = Literal["csv", "json", "xml"]

GET_GSH_2024_SALE_TRANSACTIONS_FORMAT_VALUES: set[GetGsh2024SaleTransactionsFormat] = {
    "csv",
    "json",
    "xml",
}


def check_get_gsh_2024_sale_transactions_format(
    value: str,
) -> GetGsh2024SaleTransactionsFormat:
    if value in GET_GSH_2024_SALE_TRANSACTIONS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2024_SALE_TRANSACTIONS_FORMAT_VALUES!r}"
    )
