from typing import Literal

GetGsh2023SaleTransactionsDataresource = Literal["ssfs-sale-transactions-g23"]

GET_GSH_2023_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetGsh2023SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-g23",
}


def check_get_gsh_2023_sale_transactions_dataresource(
    value: str,
) -> GetGsh2023SaleTransactionsDataresource:
    if value in GET_GSH_2023_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2023_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
