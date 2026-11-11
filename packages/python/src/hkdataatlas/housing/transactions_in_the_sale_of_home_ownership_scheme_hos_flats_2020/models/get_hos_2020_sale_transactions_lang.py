from typing import Literal

GetHos2020SaleTransactionsLang = Literal["en", "tc"]

GET_HOS_2020_SALE_TRANSACTIONS_LANG_VALUES: set[GetHos2020SaleTransactionsLang] = {
    "en",
    "tc",
}


def check_get_hos_2020_sale_transactions_lang(
    value: str,
) -> GetHos2020SaleTransactionsLang:
    if value in GET_HOS_2020_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2020_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
