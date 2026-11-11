from typing import Literal

LookupAddressGetAcceptLanguage = Literal["*", "en", "en, zh-Hant", "zh-Hant"]

LOOKUP_ADDRESS_GET_ACCEPT_LANGUAGE_VALUES: set[LookupAddressGetAcceptLanguage] = {
    "*",
    "en",
    "en, zh-Hant",
    "zh-Hant",
}


def check_lookup_address_get_accept_language(
    value: str,
) -> LookupAddressGetAcceptLanguage:
    if value in LOOKUP_ADDRESS_GET_ACCEPT_LANGUAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOOKUP_ADDRESS_GET_ACCEPT_LANGUAGE_VALUES!r}"
    )
