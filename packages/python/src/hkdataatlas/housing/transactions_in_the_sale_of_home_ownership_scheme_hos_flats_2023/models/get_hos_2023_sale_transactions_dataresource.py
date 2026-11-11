from typing import Literal

GetHos2023SaleTransactionsDataresource = Literal["ssfs-sale-transactions-023"]

GET_HOS_2023_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetHos2023SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-023",
}


def check_get_hos_2023_sale_transactions_dataresource(
    value: str,
) -> GetHos2023SaleTransactionsDataresource:
    if value in GET_HOS_2023_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2023_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
