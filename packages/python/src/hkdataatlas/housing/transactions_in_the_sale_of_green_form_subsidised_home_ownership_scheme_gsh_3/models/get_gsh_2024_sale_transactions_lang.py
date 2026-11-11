from typing import Literal

GetGsh2024SaleTransactionsLang = Literal["en", "sc", "tc"]

GET_GSH_2024_SALE_TRANSACTIONS_LANG_VALUES: set[GetGsh2024SaleTransactionsLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_gsh_2024_sale_transactions_lang(
    value: str,
) -> GetGsh2024SaleTransactionsLang:
    if value in GET_GSH_2024_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2024_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
