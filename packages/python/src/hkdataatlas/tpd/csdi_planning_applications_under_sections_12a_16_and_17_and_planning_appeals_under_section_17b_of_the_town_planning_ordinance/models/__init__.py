"""Contains all the data models used in inputs/outputs"""

from .wfs_map_server_get_feature_output_format import WfsMapServerGetFeatureOutputFormat
from .wfs_map_server_get_feature_request import WfsMapServerGetFeatureRequest
from .wfs_map_server_get_feature_service import WfsMapServerGetFeatureService
from .wfs_map_server_get_feature_version import WfsMapServerGetFeatureVersion
from .wfs_map_server_wfs_amendcrt_attributes import WfsMapServerWfsAMENDCRTAttributes
from .wfs_map_server_wfs_amendpast_attributes import WfsMapServerWfsAMENDPASTAttributes
from .wfs_map_server_wfs_appcrt_attributes import WfsMapServerWfsAPPCRTAttributes
from .wfs_map_server_wfs_apppast_attributes import WfsMapServerWfsAPPPASTAttributes
from .wfs_map_server_wfs_feature_collection import WfsMapServerWfsFeatureCollection
from .wfs_map_server_wfs_feature_collection_features_item import (
    WfsMapServerWfsFeatureCollectionFeaturesItem,
)

__all__ = (
    "WfsMapServerGetFeatureOutputFormat",
    "WfsMapServerGetFeatureRequest",
    "WfsMapServerGetFeatureService",
    "WfsMapServerGetFeatureVersion",
    "WfsMapServerWfsAMENDCRTAttributes",
    "WfsMapServerWfsAMENDPASTAttributes",
    "WfsMapServerWfsAPPCRTAttributes",
    "WfsMapServerWfsAPPPASTAttributes",
    "WfsMapServerWfsFeatureCollection",
    "WfsMapServerWfsFeatureCollectionFeaturesItem",
)
