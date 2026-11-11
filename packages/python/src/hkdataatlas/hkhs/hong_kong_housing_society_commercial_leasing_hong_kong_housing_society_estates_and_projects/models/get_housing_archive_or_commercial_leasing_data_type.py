from typing import Literal

GetHousingArchiveOrCommercialLeasingDataType = Literal["ha", "shop"]

GET_HOUSING_ARCHIVE_OR_COMMERCIAL_LEASING_DATA_TYPE_VALUES: set[
    GetHousingArchiveOrCommercialLeasingDataType
] = {
    "ha",
    "shop",
}


def check_get_housing_archive_or_commercial_leasing_data_type(
    value: str,
) -> GetHousingArchiveOrCommercialLeasingDataType:
    if value in GET_HOUSING_ARCHIVE_OR_COMMERCIAL_LEASING_DATA_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_HOUSING_ARCHIVE_OR_COMMERCIAL_LEASING_DATA_TYPE_VALUES!r}"
    )
