from typing import Literal

GetFundraisingActivitiesJsonLicence = Literal[
    "hawker", "lottery", "noncharitable", "psp"
]

GET_FUNDRAISING_ACTIVITIES_JSON_LICENCE_VALUES: set[
    GetFundraisingActivitiesJsonLicence
] = {
    "hawker",
    "lottery",
    "noncharitable",
    "psp",
}


def check_get_fundraising_activities_json_licence(
    value: str,
) -> GetFundraisingActivitiesJsonLicence:
    if value in GET_FUNDRAISING_ACTIVITIES_JSON_LICENCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FUNDRAISING_ACTIVITIES_JSON_LICENCE_VALUES!r}"
    )
