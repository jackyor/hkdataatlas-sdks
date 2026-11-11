"""Contains all the data models used in inputs/outputs"""

from .complaint_category import ComplaintCategory
from .complaint_statistics_response import ComplaintStatisticsResponse
from .complaint_year import ComplaintYear
from .get_complaint_statistics_lang import GetComplaintStatisticsLang

__all__ = (
    "ComplaintCategory",
    "ComplaintStatisticsResponse",
    "ComplaintYear",
    "GetComplaintStatisticsLang",
)
