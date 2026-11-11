from typing import Literal

GetGsh2019SaleTransactionsLang = Literal["en", "sc", "tc"]

GET_GSH_2019_SALE_TRANSACTIONS_LANG_VALUES: set[GetGsh2019SaleTransactionsLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_gsh_2019_sale_transactions_lang(
    value: str,
) -> GetGsh2019SaleTransactionsLang:
    if value in GET_GSH_2019_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2019_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
