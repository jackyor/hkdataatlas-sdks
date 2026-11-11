from typing import Literal

GetSsfsSaleTransactionsE22Dataresource = Literal["ssfs-sale-transactions-e22"]

GET_SSFS_SALE_TRANSACTIONS_E22_DATARESOURCE_VALUES: set[
    GetSsfsSaleTransactionsE22Dataresource
] = {
    "ssfs-sale-transactions-e22",
}


def check_get_ssfs_sale_transactions_e22_dataresource(
    value: str,
) -> GetSsfsSaleTransactionsE22Dataresource:
    if value in GET_SSFS_SALE_TRANSACTIONS_E22_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_SSFS_SALE_TRANSACTIONS_E22_DATARESOURCE_VALUES!r}"
    )
