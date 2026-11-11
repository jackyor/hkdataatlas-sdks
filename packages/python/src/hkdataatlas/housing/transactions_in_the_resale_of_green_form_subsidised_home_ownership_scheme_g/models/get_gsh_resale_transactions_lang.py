from typing import Literal

GetGshResaleTransactionsLang = Literal["en", "sc", "tc"]

GET_GSH_RESALE_TRANSACTIONS_LANG_VALUES: set[GetGshResaleTransactionsLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_gsh_resale_transactions_lang(value: str) -> GetGshResaleTransactionsLang:
    if value in GET_GSH_RESALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_GSH_RESALE_TRANSACTIONS_LANG_VALUES!r}"
    )
