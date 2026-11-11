from typing import Literal

GetSsfsSaleTransactionsE22Format = Literal["csv", "json", "xml"]

GET_SSFS_SALE_TRANSACTIONS_E22_FORMAT_VALUES: set[GetSsfsSaleTransactionsE22Format] = {
    "csv",
    "json",
    "xml",
}


def check_get_ssfs_sale_transactions_e22_format(
    value: str,
) -> GetSsfsSaleTransactionsE22Format:
    if value in GET_SSFS_SALE_TRANSACTIONS_E22_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_SSFS_SALE_TRANSACTIONS_E22_FORMAT_VALUES!r}"
    )
