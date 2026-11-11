from typing import Literal

GetFundraisingActivitiesXmlLicence = Literal[
    "hawker", "lottery", "noncharitable", "psp"
]

GET_FUNDRAISING_ACTIVITIES_XML_LICENCE_VALUES: set[
    GetFundraisingActivitiesXmlLicence
] = {
    "hawker",
    "lottery",
    "noncharitable",
    "psp",
}


def check_get_fundraising_activities_xml_licence(
    value: str,
) -> GetFundraisingActivitiesXmlLicence:
    if value in GET_FUNDRAISING_ACTIVITIES_XML_LICENCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FUNDRAISING_ACTIVITIES_XML_LICENCE_VALUES!r}"
    )
