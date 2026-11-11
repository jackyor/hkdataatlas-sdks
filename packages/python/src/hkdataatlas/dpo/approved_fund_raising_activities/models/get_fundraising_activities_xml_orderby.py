from typing import Literal

GetFundraisingActivitiesXmlOrderby = Literal["activity", "date", "licence"]

GET_FUNDRAISING_ACTIVITIES_XML_ORDERBY_VALUES: set[
    GetFundraisingActivitiesXmlOrderby
] = {
    "activity",
    "date",
    "licence",
}


def check_get_fundraising_activities_xml_orderby(
    value: str,
) -> GetFundraisingActivitiesXmlOrderby:
    if value in GET_FUNDRAISING_ACTIVITIES_XML_ORDERBY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FUNDRAISING_ACTIVITIES_XML_ORDERBY_VALUES!r}"
    )
