from typing import Literal

GetHos2023SaleTransactionsLang = Literal["en", "sc", "tc"]

GET_HOS_2023_SALE_TRANSACTIONS_LANG_VALUES: set[GetHos2023SaleTransactionsLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_hos_2023_sale_transactions_lang(
    value: str,
) -> GetHos2023SaleTransactionsLang:
    if value in GET_HOS_2023_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_2023_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
