from typing import Literal

GetCrdaStatisticsAgeGroup = Literal["00101", "00102", "00999"]

GET_CRDA_STATISTICS_AGE_GROUP_VALUES: set[GetCrdaStatisticsAgeGroup] = {
    "00101",
    "00102",
    "00999",
}


def check_get_crda_statistics_age_group(value: str) -> GetCrdaStatisticsAgeGroup:
    if value in GET_CRDA_STATISTICS_AGE_GROUP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CRDA_STATISTICS_AGE_GROUP_VALUES!r}"
    )
