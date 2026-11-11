from typing import Literal

LookupGeoAddressGetAcceptLanguage = Literal["*", "en", "en, zh-Hant", "zh-Hant"]

LOOKUP_GEO_ADDRESS_GET_ACCEPT_LANGUAGE_VALUES: set[
    LookupGeoAddressGetAcceptLanguage
] = {
    "*",
    "en",
    "en, zh-Hant",
    "zh-Hant",
}


def check_lookup_geo_address_get_accept_language(
    value: str,
) -> LookupGeoAddressGetAcceptLanguage:
    if value in LOOKUP_GEO_ADDRESS_GET_ACCEPT_LANGUAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOOKUP_GEO_ADDRESS_GET_ACCEPT_LANGUAGE_VALUES!r}"
    )
