from typing import Literal

GetGsh2019SaleTransactionsDataresource = Literal["ssfs-sale-transactions-g19"]

GET_GSH_2019_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetGsh2019SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-g19",
}


def check_get_gsh_2019_sale_transactions_dataresource(
    value: str,
) -> GetGsh2019SaleTransactionsDataresource:
    if value in GET_GSH_2019_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2019_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
