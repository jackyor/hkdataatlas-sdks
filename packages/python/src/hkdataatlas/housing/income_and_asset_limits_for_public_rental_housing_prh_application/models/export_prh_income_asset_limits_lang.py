from typing import Literal

ExportPrhIncomeAssetLimitsLang = Literal["en", "sc", "tc"]

EXPORT_PRH_INCOME_ASSET_LIMITS_LANG_VALUES: set[ExportPrhIncomeAssetLimitsLang] = {
    "en",
    "sc",
    "tc",
}


def check_export_prh_income_asset_limits_lang(
    value: str,
) -> ExportPrhIncomeAssetLimitsLang:
    if value in EXPORT_PRH_INCOME_ASSET_LIMITS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPORT_PRH_INCOME_ASSET_LIMITS_LANG_VALUES!r}"
    )
