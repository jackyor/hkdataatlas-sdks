"""Contains all the data models used in inputs/outputs"""

from .count import Count
from .data_record import DataRecord
from .get_statistical_table_full_series import GetStatisticalTableFullSeries
from .get_statistical_table_lang import GetStatisticalTableLang
from .header import Header
from .status import Status
from .status_code import StatusCode
from .status_name import StatusName
from .table_response import TableResponse

__all__ = (
    "Count",
    "DataRecord",
    "GetStatisticalTableFullSeries",
    "GetStatisticalTableLang",
    "Header",
    "Status",
    "StatusCode",
    "StatusName",
    "TableResponse",
)
