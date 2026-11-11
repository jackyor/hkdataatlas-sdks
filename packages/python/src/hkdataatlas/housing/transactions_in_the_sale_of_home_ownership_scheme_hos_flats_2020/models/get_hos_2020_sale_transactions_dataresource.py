from typing import Literal

GetHos2020SaleTransactionsDataresource = Literal["ssfs-sale-transactions-020"]

GET_HOS_2020_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetHos2020SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-020",
}


def check_get_hos_2020_sale_transactions_dataresource(
    value: str,
) -> GetHos2020SaleTransactionsDataresource:
    if value in GET_HOS_2020_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2020_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
