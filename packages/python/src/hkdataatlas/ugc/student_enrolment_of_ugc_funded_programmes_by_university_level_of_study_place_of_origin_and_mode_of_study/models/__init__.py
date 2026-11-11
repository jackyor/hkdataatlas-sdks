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
from .arcgis_feature_server_query_features_f import ArcgisFeatureServerQueryFeaturesF
from .publisher_dictionary_student_enrolment_data_dictionary import (
    PublisherDictionaryStudentEnrolmentDataDictionary,
)
from .publisher_dictionary_student_enrolment_data_dictionary_level_of_study_en import (
    PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyEN,
)
from .publisher_dictionary_student_enrolment_data_dictionary_level_of_study_tc import (
    PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyTC,
)
from .publisher_dictionary_student_enrolment_data_dictionary_mode_of_study_en import (
    PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyEN,
)
from .publisher_dictionary_student_enrolment_data_dictionary_mode_of_study_tc import (
    PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyTC,
)
from .publisher_dictionary_student_enrolment_data_dictionary_place_of_origin_en import (
    PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginEN,
)
from .publisher_dictionary_student_enrolment_data_dictionary_place_of_origin_tc import (
    PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginTC,
)
from .publisher_dictionary_student_enrolment_data_dictionary_university_en import (
    PublisherDictionaryStudentEnrolmentDataDictionaryUniversityEN,
)
from .publisher_dictionary_student_enrolment_data_dictionary_university_tc import (
    PublisherDictionaryStudentEnrolmentDataDictionaryUniversityTC,
)
from .wfs_map_server_get_feature_output_format import WfsMapServerGetFeatureOutputFormat
from .wfs_map_server_get_feature_request import WfsMapServerGetFeatureRequest
from .wfs_map_server_get_feature_service import WfsMapServerGetFeatureService
from .wfs_map_server_get_feature_version import WfsMapServerGetFeatureVersion
from .wfs_map_server_wfs_feature_collection import WfsMapServerWfsFeatureCollection
from .wfs_map_server_wfs_feature_collection_features_item import (
    WfsMapServerWfsFeatureCollectionFeaturesItem,
)
from .wfs_map_server_wfsgeotagging_attributes import WfsMapServerWfsgeotaggingAttributes
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
    "ArcgisFeatureServerQueryFeaturesF",
    "PublisherDictionaryStudentEnrolmentDataDictionary",
    "PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyEN",
    "PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyTC",
    "PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyEN",
    "PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyTC",
    "PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginEN",
    "PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginTC",
    "PublisherDictionaryStudentEnrolmentDataDictionaryUniversityEN",
    "PublisherDictionaryStudentEnrolmentDataDictionaryUniversityTC",
    "WfsMapServerGetFeatureOutputFormat",
    "WfsMapServerGetFeatureRequest",
    "WfsMapServerGetFeatureService",
    "WfsMapServerGetFeatureVersion",
    "WfsMapServerWfsFeatureCollection",
    "WfsMapServerWfsFeatureCollectionFeaturesItem",
    "WfsMapServerWfsgeotaggingAttributes",
    "WmsMapServerGetMapFormat",
    "WmsMapServerGetMapRequest",
    "WmsMapServerGetMapService",
    "WmsMapServerGetMapVersion",
)
