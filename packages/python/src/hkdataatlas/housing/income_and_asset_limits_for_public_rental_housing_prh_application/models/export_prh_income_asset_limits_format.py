from typing import Literal

ExportPrhIncomeAssetLimitsFormat = Literal["csv", "json", "xml"]

EXPORT_PRH_INCOME_ASSET_LIMITS_FORMAT_VALUES: set[ExportPrhIncomeAssetLimitsFormat] = {
    "csv",
    "json",
    "xml",
}


def check_export_prh_income_asset_limits_format(
    value: str,
) -> ExportPrhIncomeAssetLimitsFormat:
    if value in EXPORT_PRH_INCOME_ASSET_LIMITS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPORT_PRH_INCOME_ASSET_LIMITS_FORMAT_VALUES!r}"
    )
