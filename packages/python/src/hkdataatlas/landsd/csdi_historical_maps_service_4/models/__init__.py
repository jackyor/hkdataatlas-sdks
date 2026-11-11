"""Contains all the data models used in inputs/outputs"""

from .wms_map_server_get_map_format import WmsMapServerGetMapFormat
from .wms_map_server_get_map_request import WmsMapServerGetMapRequest
from .wms_map_server_get_map_service import WmsMapServerGetMapService
from .wms_map_server_get_map_version import WmsMapServerGetMapVersion

__all__ = (
    "WmsMapServerGetMapFormat",
    "WmsMapServerGetMapRequest",
    "WmsMapServerGetMapService",
    "WmsMapServerGetMapVersion",
)
