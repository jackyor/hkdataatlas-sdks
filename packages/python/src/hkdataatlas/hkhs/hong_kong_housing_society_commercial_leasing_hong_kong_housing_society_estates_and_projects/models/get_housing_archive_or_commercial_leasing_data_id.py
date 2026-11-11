from typing import Literal

GetHousingArchiveOrCommercialLeasingDataId = Literal[
    "1", "10", "2", "3", "4_5", "6", "7", "8", "9"
]

GET_HOUSING_ARCHIVE_OR_COMMERCIAL_LEASING_DATA_ID_VALUES: set[
    GetHousingArchiveOrCommercialLeasingDataId
] = {
    "1",
    "10",
    "2",
    "3",
    "4_5",
    "6",
    "7",
    "8",
    "9",
}


def check_get_housing_archive_or_commercial_leasing_data_id(
    value: str,
) -> GetHousingArchiveOrCommercialLeasingDataId:
    if value in GET_HOUSING_ARCHIVE_OR_COMMERCIAL_LEASING_DATA_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOUSING_ARCHIVE_OR_COMMERCIAL_LEASING_DATA_ID_VALUES!r}"
    )
