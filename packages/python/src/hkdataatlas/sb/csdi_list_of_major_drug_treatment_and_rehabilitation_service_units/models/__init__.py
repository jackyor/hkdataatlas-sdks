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
from .arcgis_feature_server_arcgis_layer_1_attributes import (
    ArcgisFeatureServerArcgisLayer1Attributes,
)
from .arcgis_feature_server_arcgis_layer_2_attributes import (
    ArcgisFeatureServerArcgisLayer2Attributes,
)
from .arcgis_feature_server_arcgis_layer_3_attributes import (
    ArcgisFeatureServerArcgisLayer3Attributes,
)
from .arcgis_feature_server_arcgis_layer_4_attributes import (
    ArcgisFeatureServerArcgisLayer4Attributes,
)
from .arcgis_feature_server_query_features_f import ArcgisFeatureServerQueryFeaturesF
from .wfs_map_server_get_feature_output_format import WfsMapServerGetFeatureOutputFormat
from .wfs_map_server_get_feature_request import WfsMapServerGetFeatureRequest
from .wfs_map_server_get_feature_service import WfsMapServerGetFeatureService
from .wfs_map_server_get_feature_version import WfsMapServerGetFeatureVersion
from .wfs_map_server_wfs_ccps_as_attributes import WfsMapServerWfsCCPSAsAttributes
from .wfs_map_server_wfs_cd_cs_attributes import WfsMapServerWfsCDCsAttributes
from .wfs_map_server_wfs_dat_cs_attributes import WfsMapServerWfsDATCsAttributes
from .wfs_map_server_wfs_feature_collection import WfsMapServerWfsFeatureCollection
from .wfs_map_server_wfs_feature_collection_features_item import (
    WfsMapServerWfsFeatureCollectionFeaturesItem,
)
from .wfs_map_server_wfs_m_cs_attributes import WfsMapServerWfsMCsAttributes
from .wfs_map_server_wfs_sa_cs_attributes import WfsMapServerWfsSACsAttributes
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
    "ArcgisFeatureServerArcgisLayer1Attributes",
    "ArcgisFeatureServerArcgisLayer2Attributes",
    "ArcgisFeatureServerArcgisLayer3Attributes",
    "ArcgisFeatureServerArcgisLayer4Attributes",
    "ArcgisFeatureServerQueryFeaturesF",
    "WfsMapServerGetFeatureOutputFormat",
    "WfsMapServerGetFeatureRequest",
    "WfsMapServerGetFeatureService",
    "WfsMapServerGetFeatureVersion",
    "WfsMapServerWfsCCPSAsAttributes",
    "WfsMapServerWfsCDCsAttributes",
    "WfsMapServerWfsDATCsAttributes",
    "WfsMapServerWfsFeatureCollection",
    "WfsMapServerWfsFeatureCollectionFeaturesItem",
    "WfsMapServerWfsMCsAttributes",
    "WfsMapServerWfsSACsAttributes",
    "WmsMapServerGetMapFormat",
    "WmsMapServerGetMapRequest",
    "WmsMapServerGetMapService",
    "WmsMapServerGetMapVersion",
)
