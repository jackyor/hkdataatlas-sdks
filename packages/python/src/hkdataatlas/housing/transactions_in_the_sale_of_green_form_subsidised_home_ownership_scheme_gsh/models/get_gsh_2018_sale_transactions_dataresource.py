from typing import Literal

GetGsh2018SaleTransactionsDataresource = Literal["ssfs-sale-transactions-G18"]

GET_GSH_2018_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetGsh2018SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-G18",
}


def check_get_gsh_2018_sale_transactions_dataresource(
    value: str,
) -> GetGsh2018SaleTransactionsDataresource:
    if value in GET_GSH_2018_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2018_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
