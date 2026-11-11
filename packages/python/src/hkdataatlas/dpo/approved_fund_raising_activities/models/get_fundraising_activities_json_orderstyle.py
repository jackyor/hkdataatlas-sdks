from typing import Literal

GetFundraisingActivitiesJsonOrderstyle = Literal["asc", "desc"]

GET_FUNDRAISING_ACTIVITIES_JSON_ORDERSTYLE_VALUES: set[
    GetFundraisingActivitiesJsonOrderstyle
] = {
    "asc",
    "desc",
}


def check_get_fundraising_activities_json_orderstyle(
    value: str,
) -> GetFundraisingActivitiesJsonOrderstyle:
    if value in GET_FUNDRAISING_ACTIVITIES_JSON_ORDERSTYLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FUNDRAISING_ACTIVITIES_JSON_ORDERSTYLE_VALUES!r}"
    )
