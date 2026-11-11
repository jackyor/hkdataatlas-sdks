from typing import Literal

GetHosFlats2024SaleTransactionsLang = Literal["en", "sc", "tc"]

GET_HOS_FLATS_2024_SALE_TRANSACTIONS_LANG_VALUES: set[
    GetHosFlats2024SaleTransactionsLang
] = {
    "en",
    "sc",
    "tc",
}


def check_get_hos_flats_2024_sale_transactions_lang(
    value: str,
) -> GetHosFlats2024SaleTransactionsLang:
    if value in GET_HOS_FLATS_2024_SALE_TRANSACTIONS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOS_FLATS_2024_SALE_TRANSACTIONS_LANG_VALUES!r}"
    )
