from typing import Literal

GetTpsSaleTransactionsLang = Literal["en", "tc"]

GET_TPS_SALE_TRANSACTIONS_LANG_VALUES: set[GetTpsSaleTransactionsLang] = {
    "en",
    "tc",
}


def check_get_tps_sale_transactions_lang(value: str) -> GetTpsSaleTransactionsLang:
    if value in GET_TPS_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TPS_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
