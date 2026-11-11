from typing import Literal

GetFundraisingActivitiesJsonActivity = Literal[
    "flag", "fund", "lotpri", "lotpub", "noncharitable", "sell"
]

GET_FUNDRAISING_ACTIVITIES_JSON_ACTIVITY_VALUES: set[
    GetFundraisingActivitiesJsonActivity
] = {
    "flag",
    "fund",
    "lotpri",
    "lotpub",
    "noncharitable",
    "sell",
}


def check_get_fundraising_activities_json_activity(
    value: str,
) -> GetFundraisingActivitiesJsonActivity:
    if value in GET_FUNDRAISING_ACTIVITIES_JSON_ACTIVITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FUNDRAISING_ACTIVITIES_JSON_ACTIVITY_VALUES!r}"
    )
