from typing import Literal

GetGshResaleTransactionsFormat = Literal["csv", "json", "xml"]

GET_GSH_RESALE_TRANSACTIONS_FORMAT_VALUES: set[GetGshResaleTransactionsFormat] = {
    "csv",
    "json",
    "xml",
}


def check_get_gsh_resale_transactions_format(
    value: str,
) -> GetGshResaleTransactionsFormat:
    if value in GET_GSH_RESALE_TRANSACTIONS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_RESALE_TRANSACTIONS_FORMAT_VALUES!r}"
    )
