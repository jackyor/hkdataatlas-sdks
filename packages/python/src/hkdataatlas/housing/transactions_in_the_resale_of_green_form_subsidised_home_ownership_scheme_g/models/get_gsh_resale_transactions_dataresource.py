from typing import Literal

GetGshResaleTransactionsDataresource = Literal["ssfs-sale-transactions-e23"]

GET_GSH_RESALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetGshResaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-e23",
}


def check_get_gsh_resale_transactions_dataresource(
    value: str,
) -> GetGshResaleTransactionsDataresource:
    if value in GET_GSH_RESALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_RESALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
