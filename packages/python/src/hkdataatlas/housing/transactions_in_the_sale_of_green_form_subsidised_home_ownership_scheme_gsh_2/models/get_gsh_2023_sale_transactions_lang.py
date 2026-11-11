from typing import Literal

GetGsh2023SaleTransactionsLang = Literal["en", "sc", "tc"]

GET_GSH_2023_SALE_TRANSACTIONS_LANG_VALUES: set[GetGsh2023SaleTransactionsLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_gsh_2023_sale_transactions_lang(
    value: str,
) -> GetGsh2023SaleTransactionsLang:
    if value in GET_GSH_2023_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2023_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
