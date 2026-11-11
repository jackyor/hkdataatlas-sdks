"""Contains all the data models used in inputs/outputs"""

from .get_register_ambs_lang import GetRegisterAmbsLang
from .get_register_ambs_response_200 import GetRegisterAmbsResponse200
from .get_register_ambs_response_200_records_item import (
    GetRegisterAmbsResponse200RecordsItem,
)
from .get_register_ambs_response_200_result import GetRegisterAmbsResponse200Result

__all__ = (
    "GetRegisterAmbsLang",
    "GetRegisterAmbsResponse200",
    "GetRegisterAmbsResponse200RecordsItem",
    "GetRegisterAmbsResponse200Result",
)
