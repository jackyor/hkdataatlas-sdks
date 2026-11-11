from typing import Literal

GetFundraisingActivitiesXmlActivity = Literal[
    "flag", "fund", "lotpri", "lotpub", "noncharitable", "sell"
]

GET_FUNDRAISING_ACTIVITIES_XML_ACTIVITY_VALUES: set[
    GetFundraisingActivitiesXmlActivity
] = {
    "flag",
    "fund",
    "lotpri",
    "lotpub",
    "noncharitable",
    "sell",
}


def check_get_fundraising_activities_xml_activity(
    value: str,
) -> GetFundraisingActivitiesXmlActivity:
    if value in GET_FUNDRAISING_ACTIVITIES_XML_ACTIVITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FUNDRAISING_ACTIVITIES_XML_ACTIVITY_VALUES!r}"
    )
