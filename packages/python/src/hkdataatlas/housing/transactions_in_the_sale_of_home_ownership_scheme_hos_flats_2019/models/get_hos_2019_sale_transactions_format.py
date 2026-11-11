from typing import Literal

GetHos2019SaleTransactionsFormat = Literal["csv", "json", "xml"]

GET_HOS_2019_SALE_TRANSACTIONS_FORMAT_VALUES: set[GetHos2019SaleTransactionsFormat] = {
    "csv",
    "json",
    "xml",
}


def check_get_hos_2019_sale_transactions_format(
    value: str,
) -> GetHos2019SaleTransactionsFormat:
    if value in GET_HOS_2019_SALE_TRANSACTIONS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2019_SALE_TRANSACTIONS_FORMAT_VALUES!r}"
    )
