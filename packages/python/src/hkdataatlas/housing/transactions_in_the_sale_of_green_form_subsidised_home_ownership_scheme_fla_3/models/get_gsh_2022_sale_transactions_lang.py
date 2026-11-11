from typing import Literal

GetGsh2022SaleTransactionsLang = Literal["en", "sc", "tc"]

GET_GSH_2022_SALE_TRANSACTIONS_LANG_VALUES: set[GetGsh2022SaleTransactionsLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_gsh_2022_sale_transactions_lang(
    value: str,
) -> GetGsh2022SaleTransactionsLang:
    if value in GET_GSH_2022_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2022_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
