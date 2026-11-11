from typing import Literal

GetStatisticalTableFullSeries = Literal["1"]

GET_STATISTICAL_TABLE_FULL_SERIES_VALUES: set[GetStatisticalTableFullSeries] = {
    "1",
}


def check_get_statistical_table_full_series(
    value: str,
) -> GetStatisticalTableFullSeries:
    if value in GET_STATISTICAL_TABLE_FULL_SERIES_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_STATISTICAL_TABLE_FULL_SERIES_VALUES!r}"
    )
