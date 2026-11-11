from typing import Literal

GetHos2022SaleTransactionsDataresource = Literal["ssfs-sale-transactions-022"]

GET_HOS_2022_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetHos2022SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-022",
}


def check_get_hos_2022_sale_transactions_dataresource(
    value: str,
) -> GetHos2022SaleTransactionsDataresource:
    if value in GET_HOS_2022_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2022_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
