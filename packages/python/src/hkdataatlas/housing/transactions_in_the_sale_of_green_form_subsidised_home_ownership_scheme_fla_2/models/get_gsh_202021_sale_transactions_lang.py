from typing import Literal

GetGsh202021SaleTransactionsLang = Literal["en", "tc"]

GET_GSH_202021_SALE_TRANSACTIONS_LANG_VALUES: set[GetGsh202021SaleTransactionsLang] = {
    "en",
    "tc",
}


def check_get_gsh_202021_sale_transactions_lang(
    value: str,
) -> GetGsh202021SaleTransactionsLang:
    if value in GET_GSH_202021_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_202021_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
