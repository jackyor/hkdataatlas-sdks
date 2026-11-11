from typing import Literal

ExportLightPublicHousingStockLang = Literal["en"]

EXPORT_LIGHT_PUBLIC_HOUSING_STOCK_LANG_VALUES: set[
    ExportLightPublicHousingStockLang
] = {
    "en",
}


def check_export_light_public_housing_stock_lang(
    value: str,
) -> ExportLightPublicHousingStockLang:
    if value in EXPORT_LIGHT_PUBLIC_HOUSING_STOCK_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPORT_LIGHT_PUBLIC_HOUSING_STOCK_LANG_VALUES!r}"
    )
