from typing import Literal

GetHosFlats2024SaleTransactionsDataresource = Literal["ssfs-sale-transactions-024"]

GET_HOS_FLATS_2024_SALE_TRANSACTIONS_DATARESOURCE_VALUES: set[
    GetHosFlats2024SaleTransactionsDataresource
] = {
    "ssfs-sale-transactions-024",
}


def check_get_hos_flats_2024_sale_transactions_dataresource(
    value: str,
) -> GetHosFlats2024SaleTransactionsDataresource:
    if value in GET_HOS_FLATS_2024_SALE_TRANSACTIONS_DATARESOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_FLATS_2024_SALE_TRANSACTIONS_DATARESOURCE_VALUES!r}"
    )
