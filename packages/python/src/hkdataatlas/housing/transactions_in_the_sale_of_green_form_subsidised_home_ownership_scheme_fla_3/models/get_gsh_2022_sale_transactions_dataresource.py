from typing import Literal

GetGsh2022SaleTransactionsDataresource = Literal["ssfs-sale-transactions-g22"]

GET_GSH_2022_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetGsh2022SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-g22",
}


def check_get_gsh_2022_sale_transactions_dataresource(
    value: str,
) -> GetGsh2022SaleTransactionsDataresource:
    if value in GET_GSH_2022_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2022_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
