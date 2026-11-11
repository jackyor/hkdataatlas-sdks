from typing import Literal

GetHos2023SaleTransactionsFormat = Literal["csv", "json", "xml"]

GET_HOS_2023_SALE_TRANSACTIONS_FORMAT_VALUES: set[GetHos2023SaleTransactionsFormat] = {
    "csv",
    "json",
    "xml",
}


def check_get_hos_2023_sale_transactions_format(
    value: str,
) -> GetHos2023SaleTransactionsFormat:
    if value in GET_HOS_2023_SALE_TRANSACTIONS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2023_SALE_TRANSACTIONS_FORMAT_VALUES!r}"
    )
