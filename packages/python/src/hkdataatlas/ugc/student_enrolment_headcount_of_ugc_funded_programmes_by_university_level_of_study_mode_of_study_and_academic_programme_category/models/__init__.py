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
from .publisher_dictionary_student_enrolment_headcount_data_dictionary import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionary,
)
from .publisher_dictionary_student_enrolment_headcount_data_dictionary_academic_programme_category_en import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryEN,
)
from .publisher_dictionary_student_enrolment_headcount_data_dictionary_academic_programme_category_tc import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryTC,
)
from .publisher_dictionary_student_enrolment_headcount_data_dictionary_level_of_study_en import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyEN,
)
from .publisher_dictionary_student_enrolment_headcount_data_dictionary_level_of_study_tc import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyTC,
)
from .publisher_dictionary_student_enrolment_headcount_data_dictionary_mode_of_study_en import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyEN,
)
from .publisher_dictionary_student_enrolment_headcount_data_dictionary_mode_of_study_tc import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyTC,
)
from .publisher_dictionary_student_enrolment_headcount_data_dictionary_university_en import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityEN,
)
from .publisher_dictionary_student_enrolment_headcount_data_dictionary_university_tc import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityTC,
)
from .wfs_map_server_get_feature_output_format import WfsMapServerGetFeatureOutputFormat
from .wfs_map_server_get_feature_request import WfsMapServerGetFeatureRequest
from .wfs_map_server_get_feature_service import WfsMapServerGetFeatureService
from .wfs_map_server_get_feature_version import WfsMapServerGetFeatureVersion
from .wfs_map_server_wfs_feature_collection import WfsMapServerWfsFeatureCollection
from .wfs_map_server_wfs_feature_collection_features_item import (
    WfsMapServerWfsFeatureCollectionFeaturesItem,
)

__all__ = (
    "ArcgisFeatureServerArcgisFeatureSet",
    "ArcgisFeatureServerArcgisFeatureSetFeaturesItem",
    "ArcgisFeatureServerArcgisGeoJson",
    "ArcgisFeatureServerArcgisGeoJsonFeaturesItem",
    "ArcgisFeatureServerArcgisJsonEnvelope",
    "ArcgisFeatureServerArcgisJsonEnvelopeFeaturesItem",
    "ArcgisFeatureServerArcgisLayer0Attributes",
    "ArcgisFeatureServerQueryFeaturesF",
    "PublisherDictionaryStudentEnrolmentHeadcountDataDictionary",
    "PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryEN",
    "PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryTC",
    "PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyEN",
    "PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyTC",
    "PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyEN",
    "PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyTC",
    "PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityEN",
    "PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityTC",
    "WfsMapServerGetFeatureOutputFormat",
    "WfsMapServerGetFeatureRequest",
    "WfsMapServerGetFeatureService",
    "WfsMapServerGetFeatureVersion",
    "WfsMapServerWfsFeatureCollection",
    "WfsMapServerWfsFeatureCollectionFeaturesItem",
)
