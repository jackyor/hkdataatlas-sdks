from typing import Literal

GetFundraisingActivitiesXmlCharitable = Literal[0, 1]

GET_FUNDRAISING_ACTIVITIES_XML_CHARITABLE_VALUES: set[
    GetFundraisingActivitiesXmlCharitable
] = {
    0,
    1,
}


def check_get_fundraising_activities_xml_charitable(
    value: int,
) -> GetFundraisingActivitiesXmlCharitable:
    if value in GET_FUNDRAISING_ACTIVITIES_XML_CHARITABLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FUNDRAISING_ACTIVITIES_XML_CHARITABLE_VALUES!r}"
    )
