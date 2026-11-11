from typing import Literal

GetGsh2024SaleTransactionsDataresource = Literal["ssfs-sale-transactions-g24"]

GET_GSH_2024_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetGsh2024SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-g24",
}


def check_get_gsh_2024_sale_transactions_dataresource(
    value: str,
) -> GetGsh2024SaleTransactionsDataresource:
    if value in GET_GSH_2024_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2024_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
