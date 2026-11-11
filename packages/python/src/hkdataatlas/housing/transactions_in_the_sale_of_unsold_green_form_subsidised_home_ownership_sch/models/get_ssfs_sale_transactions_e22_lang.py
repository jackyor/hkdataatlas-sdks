from typing import Literal

GetSsfsSaleTransactionsE22Lang = Literal["en", "sc", "tc"]

GET_SSFS_SALE_TRANSACTIONS_E22_LANG_VALUES: set[GetSsfsSaleTransactionsE22Lang] = {
    "en",
    "sc",
    "tc",
}


def check_get_ssfs_sale_transactions_e22_lang(
    value: str,
) -> GetSsfsSaleTransactionsE22Lang:
    if value in GET_SSFS_SALE_TRANSACTIONS_E22_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_SSFS_SALE_TRANSACTIONS_E22_LANG_VALUES!r}"
    )
