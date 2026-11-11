from typing import Literal

GetHos2019SaleTransactionsDataresource = Literal["ssfs-sale-transactions-019"]

GET_HOS_2019_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetHos2019SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-019",
}


def check_get_hos_2019_sale_transactions_dataresource(
    value: str,
) -> GetHos2019SaleTransactionsDataresource:
    if value in GET_HOS_2019_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2019_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
