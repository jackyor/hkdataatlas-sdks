from typing import Literal

GetTpsSaleTransactionsDataresource = Literal["tps_sale_transactions"]

GET_TPS_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetTpsSaleTransactionsDataresource
] = {
    "tps_sale_transactions",
}


def check_get_tps_sale_transactions_dataresource(
    value: str,
) -> GetTpsSaleTransactionsDataresource:
    if value in GET_TPS_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TPS_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
