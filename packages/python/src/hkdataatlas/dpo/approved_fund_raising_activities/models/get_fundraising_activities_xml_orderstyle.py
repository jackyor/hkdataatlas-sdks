from typing import Literal

GetFundraisingActivitiesXmlOrderstyle = Literal["asc", "desc"]

GET_FUNDRAISING_ACTIVITIES_XML_ORDERSTYLE_VALUES: set[
    GetFundraisingActivitiesXmlOrderstyle
] = {
    "asc",
    "desc",
}


def check_get_fundraising_activities_xml_orderstyle(
    value: str,
) -> GetFundraisingActivitiesXmlOrderstyle:
    if value in GET_FUNDRAISING_ACTIVITIES_XML_ORDERSTYLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FUNDRAISING_ACTIVITIES_XML_ORDERSTYLE_VALUES!r}"
    )
