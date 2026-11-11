from typing import Literal

GetHosFlats2024SaleTransactionsFormat = Literal["csv", "json", "xml"]

GET_HOS_FLATS_2024_SALE_TRANSACTIONS_FORMAT_VALUES: set[
    GetHosFlats2024SaleTransactionsFormat
] = {
    "csv",
    "json",
    "xml",
}


def check_get_hos_flats_2024_sale_transactions_format(
    value: str,
) -> GetHosFlats2024SaleTransactionsFormat:
    if value in GET_HOS_FLATS_2024_SALE_TRANSACTIONS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_FLATS_2024_SALE_TRANSACTIONS_FORMAT_VALUES!r}"
    )
