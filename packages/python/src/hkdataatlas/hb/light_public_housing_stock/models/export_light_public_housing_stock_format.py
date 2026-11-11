from typing import Literal

ExportLightPublicHousingStockFormat = Literal["csv", "json", "xml"]

EXPORT_LIGHT_PUBLIC_HOUSING_STOCK_FORMAT_VALUES: set[
    ExportLightPublicHousingStockFormat
] = {
    "csv",
    "json",
    "xml",
}


def check_export_light_public_housing_stock_format(
    value: str,
) -> ExportLightPublicHousingStockFormat:
    if value in EXPORT_LIGHT_PUBLIC_HOUSING_STOCK_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPORT_LIGHT_PUBLIC_HOUSING_STOCK_FORMAT_VALUES!r}"
    )
