from typing import Literal

GetHos2022SaleTransactionsLang = Literal["en", "sc", "tc"]

GET_HOS_2022_SALE_TRANSACTIONS_LANG_VALUES: set[GetHos2022SaleTransactionsLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_hos_2022_sale_transactions_lang(
    value: str,
) -> GetHos2022SaleTransactionsLang:
    if value in GET_HOS_2022_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2022_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
