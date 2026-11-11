from typing import Literal

GetHos2018SaleTransactionsLang = Literal["en", "tc"]

GET_HOS_2018_SALE_TRANSACTIONS_LANG_VALUES: set[GetHos2018SaleTransactionsLang] = {
    "en",
    "tc",
}


def check_get_hos_2018_sale_transactions_lang(
    value: str,
) -> GetHos2018SaleTransactionsLang:
    if value in GET_HOS_2018_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2018_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
