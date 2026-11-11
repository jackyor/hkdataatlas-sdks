"""Contains all the data models used in inputs/outputs"""

from .activity import Activity
from .fundraising_response import FundraisingResponse
from .get_fundraising_activities_json_activity import (
    GetFundraisingActivitiesJsonActivity,
)
from .get_fundraising_activities_json_charitable import (
    GetFundraisingActivitiesJsonCharitable,
)
from .get_fundraising_activities_json_licence import GetFundraisingActivitiesJsonLicence
from .get_fundraising_activities_json_orderby import GetFundraisingActivitiesJsonOrderby
from .get_fundraising_activities_json_orderstyle import (
    GetFundraisingActivitiesJsonOrderstyle,
)
from .get_fundraising_activities_xml_activity import GetFundraisingActivitiesXmlActivity
from .get_fundraising_activities_xml_charitable import (
    GetFundraisingActivitiesXmlCharitable,
)
from .get_fundraising_activities_xml_licence import GetFundraisingActivitiesXmlLicence
from .get_fundraising_activities_xml_orderby import GetFundraisingActivitiesXmlOrderby
from .get_fundraising_activities_xml_orderstyle import (
    GetFundraisingActivitiesXmlOrderstyle,
)
from .remark_legend import RemarkLegend
from .schedule import Schedule

__all__ = (
    "Activity",
    "FundraisingResponse",
    "GetFundraisingActivitiesJsonActivity",
    "GetFundraisingActivitiesJsonCharitable",
    "GetFundraisingActivitiesJsonLicence",
    "GetFundraisingActivitiesJsonOrderby",
    "GetFundraisingActivitiesJsonOrderstyle",
    "GetFundraisingActivitiesXmlActivity",
    "GetFundraisingActivitiesXmlCharitable",
    "GetFundraisingActivitiesXmlLicence",
    "GetFundraisingActivitiesXmlOrderby",
    "GetFundraisingActivitiesXmlOrderstyle",
    "RemarkLegend",
    "Schedule",
)
