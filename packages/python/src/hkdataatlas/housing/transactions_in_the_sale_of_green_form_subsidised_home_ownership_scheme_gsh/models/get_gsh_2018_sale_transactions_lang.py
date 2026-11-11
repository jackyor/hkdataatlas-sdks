from typing import Literal

GetGsh2018SaleTransactionsLang = Literal["en", "tc"]

GET_GSH_2018_SALE_TRANSACTIONS_LANG_VALUES: set[GetGsh2018SaleTransactionsLang] = {
    "en",
    "tc",
}


def check_get_gsh_2018_sale_transactions_lang(
    value: str,
) -> GetGsh2018SaleTransactionsLang:
    if value in GET_GSH_2018_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_2018_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
