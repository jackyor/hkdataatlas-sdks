from typing import Literal

GetFundraisingActivitiesJsonOrderby = Literal["activity", "date", "licence"]

GET_FUNDRAISING_ACTIVITIES_JSON_ORDERBY_VALUES: set[
    GetFundraisingActivitiesJsonOrderby
] = {
    "activity",
    "date",
    "licence",
}


def check_get_fundraising_activities_json_orderby(
    value: str,
) -> GetFundraisingActivitiesJsonOrderby:
    if value in GET_FUNDRAISING_ACTIVITIES_JSON_ORDERBY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FUNDRAISING_ACTIVITIES_JSON_ORDERBY_VALUES!r}"
    )
