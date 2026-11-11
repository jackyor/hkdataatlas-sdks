from typing import Literal

GetHos2019SaleTransactionsLang = Literal["en", "sc", "tc"]

GET_HOS_2019_SALE_TRANSACTIONS_LANG_VALUES: set[GetHos2019SaleTransactionsLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_hos_2019_sale_transactions_lang(
    value: str,
) -> GetHos2019SaleTransactionsLang:
    if value in GET_HOS_2019_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2019_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
