"""Contains all the data models used in inputs/outputs"""

from .arcgis_feature_server_arcgis_feature_set import (
    ArcgisFeatureServerArcgisFeatureSet,
)
from .arcgis_feature_server_arcgis_feature_set_features_item import (
    ArcgisFeatureServerArcgisFeatureSetFeaturesItem,
)
from .arcgis_feature_server_arcgis_geo_json import ArcgisFeatureServerArcgisGeoJson
from .arcgis_feature_server_arcgis_geo_json_features_item import (
    ArcgisFeatureServerArcgisGeoJsonFeaturesItem,
)
from .arcgis_feature_server_arcgis_json_envelope import (
    ArcgisFeatureServerArcgisJsonEnvelope,
)
from .arcgis_feature_server_arcgis_json_envelope_features_item import (
    ArcgisFeatureServerArcgisJsonEnvelopeFeaturesItem,
)
from .arcgis_feature_server_arcgis_layer_0_attributes import (
    ArcgisFeatureServerArcgisLayer0Attributes,
)
from .arcgis_feature_server_arcgis_layer_1000_attributes import (
    ArcgisFeatureServerArcgisLayer1000Attributes,
)
from .arcgis_feature_server_arcgis_layer_1001_attributes import (
    ArcgisFeatureServerArcgisLayer1001Attributes,
)
from .arcgis_feature_server_arcgis_layer_1002_attributes import (
    ArcgisFeatureServerArcgisLayer1002Attributes,
)
from .arcgis_feature_server_arcgis_layer_1003_attributes import (
    ArcgisFeatureServerArcgisLayer1003Attributes,
)
from .arcgis_feature_server_arcgis_layer_1004_attributes import (
    ArcgisFeatureServerArcgisLayer1004Attributes,
)
from .arcgis_feature_server_arcgis_layer_1005_attributes import (
    ArcgisFeatureServerArcgisLayer1005Attributes,
)
from .arcgis_feature_server_query_features_f import ArcgisFeatureServerQueryFeaturesF
from .wfs_map_server_get_feature_output_format import WfsMapServerGetFeatureOutputFormat
from .wfs_map_server_get_feature_request import WfsMapServerGetFeatureRequest
from .wfs_map_server_get_feature_service import WfsMapServerGetFeatureService
from .wfs_map_server_get_feature_version import WfsMapServerGetFeatureVersion
from .wfs_map_server_wfs_building_attributes import WfsMapServerWfsBuildingAttributes
from .wfs_map_server_wfs_building_lot_no_info_attributes import (
    WfsMapServerWfsBuildingLotNoInfoAttributes,
)
from .wfs_map_server_wfs_building_name_attributes import (
    WfsMapServerWfsBuildingNameAttributes,
)
from .wfs_map_server_wfs_building_relate_op_structure_attributes import (
    WfsMapServerWfsBuildingRelateOPStructureAttributes,
)
from .wfs_map_server_wfs_building_works_history_attributes import (
    WfsMapServerWfsBuildingWorksHistoryAttributes,
)
from .wfs_map_server_wfs_feature_collection import WfsMapServerWfsFeatureCollection
from .wfs_map_server_wfs_feature_collection_features_item import (
    WfsMapServerWfsFeatureCollectionFeaturesItem,
)
from .wfs_map_server_wfs_op_attributes import WfsMapServerWfsOPAttributes
from .wfs_map_server_wfs_op_structure_attributes import (
    WfsMapServerWfsOPStructureAttributes,
)
from .wms_map_server_get_map_format import WmsMapServerGetMapFormat
from .wms_map_server_get_map_request import WmsMapServerGetMapRequest
from .wms_map_server_get_map_service import WmsMapServerGetMapService
from .wms_map_server_get_map_version import WmsMapServerGetMapVersion

__all__ = (
    "ArcgisFeatureServerArcgisFeatureSet",
    "ArcgisFeatureServerArcgisFeatureSetFeaturesItem",
    "ArcgisFeatureServerArcgisGeoJson",
    "ArcgisFeatureServerArcgisGeoJsonFeaturesItem",
    "ArcgisFeatureServerArcgisJsonEnvelope",
    "ArcgisFeatureServerArcgisJsonEnvelopeFeaturesItem",
    "ArcgisFeatureServerArcgisLayer0Attributes",
    "ArcgisFeatureServerArcgisLayer1000Attributes",
    "ArcgisFeatureServerArcgisLayer1001Attributes",
    "ArcgisFeatureServerArcgisLayer1002Attributes",
    "ArcgisFeatureServerArcgisLayer1003Attributes",
    "ArcgisFeatureServerArcgisLayer1004Attributes",
    "ArcgisFeatureServerArcgisLayer1005Attributes",
    "ArcgisFeatureServerQueryFeaturesF",
    "WfsMapServerGetFeatureOutputFormat",
    "WfsMapServerGetFeatureRequest",
    "WfsMapServerGetFeatureService",
    "WfsMapServerGetFeatureVersion",
    "WfsMapServerWfsBuildingAttributes",
    "WfsMapServerWfsBuildingLotNoInfoAttributes",
    "WfsMapServerWfsBuildingNameAttributes",
    "WfsMapServerWfsBuildingRelateOPStructureAttributes",
    "WfsMapServerWfsBuildingWorksHistoryAttributes",
    "WfsMapServerWfsFeatureCollection",
    "WfsMapServerWfsFeatureCollectionFeaturesItem",
    "WfsMapServerWfsOPAttributes",
    "WfsMapServerWfsOPStructureAttributes",
    "WmsMapServerGetMapFormat",
    "WmsMapServerGetMapRequest",
    "WmsMapServerGetMapService",
    "WmsMapServerGetMapVersion",
)
