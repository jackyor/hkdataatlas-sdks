from typing import Literal

GetFundraisingActivitiesJsonCharitable = Literal[0, 1]

GET_FUNDRAISING_ACTIVITIES_JSON_CHARITABLE_VALUES: set[
    GetFundraisingActivitiesJsonCharitable
] = {
    0,
    1,
}


def check_get_fundraising_activities_json_charitable(
    value: int,
) -> GetFundraisingActivitiesJsonCharitable:
    if value in GET_FUNDRAISING_ACTIVITIES_JSON_CHARITABLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FUNDRAISING_ACTIVITIES_JSON_CHARITABLE_VALUES!r}"
    )
