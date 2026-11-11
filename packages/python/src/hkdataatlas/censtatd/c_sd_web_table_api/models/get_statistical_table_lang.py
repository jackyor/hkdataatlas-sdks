from typing import Literal

GetStatisticalTableLang = Literal["en", "sc", "tc"]

GET_STATISTICAL_TABLE_LANG_VALUES: set[GetStatisticalTableLang] = {
    "en",
    "sc",
    "tc",
}


def check_get_statistical_table_lang(value: str) -> GetStatisticalTableLang:
    if value in GET_STATISTICAL_TABLE_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_STATISTICAL_TABLE_LANG_VALUES!r}"
    )
