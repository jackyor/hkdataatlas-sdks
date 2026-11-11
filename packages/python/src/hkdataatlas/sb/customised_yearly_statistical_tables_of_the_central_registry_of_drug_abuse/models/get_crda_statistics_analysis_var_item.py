from typing import Literal

GetCrdaStatisticsAnalysisVarItem = Literal[
    "CT000305",
    "CT000308",
    "CT000310",
    "CT000312",
    "CT000313",
    "CT000314",
    "CT000315",
    "CT000318",
    "CT000320",
    "CT000341",
    "CT000439",
    "CT000440",
]

GET_CRDA_STATISTICS_ANALYSIS_VAR_ITEM_VALUES: set[GetCrdaStatisticsAnalysisVarItem] = {
    "CT000305",
    "CT000308",
    "CT000310",
    "CT000312",
    "CT000313",
    "CT000314",
    "CT000315",
    "CT000318",
    "CT000320",
    "CT000341",
    "CT000439",
    "CT000440",
}


def check_get_crda_statistics_analysis_var_item(
    value: str,
) -> GetCrdaStatisticsAnalysisVarItem:
    if value in GET_CRDA_STATISTICS_ANALYSIS_VAR_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CRDA_STATISTICS_ANALYSIS_VAR_ITEM_VALUES!r}"
    )
