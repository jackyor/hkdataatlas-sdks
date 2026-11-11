from typing import Literal

GetGsh202021SaleTransactionsDataresource = Literal["ssfs-sale-transactions-g20"]

GET_GSH_202021_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetGsh202021SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-g20",
}


def check_get_gsh_202021_sale_transactions_dataresource(
    value: str,
) -> GetGsh202021SaleTransactionsDataresource:
    if value in GET_GSH_202021_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_202021_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
