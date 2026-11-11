from typing import Literal

GetHos2018SaleTransactionsDataresource = Literal["ssfs-sale-transactions-018"]

GET_HOS_2018_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetHos2018SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-018",
}


def check_get_hos_2018_sale_transactions_dataresource(
    value: str,
) -> GetHos2018SaleTransactionsDataresource:
    if value in GET_HOS_2018_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2018_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
