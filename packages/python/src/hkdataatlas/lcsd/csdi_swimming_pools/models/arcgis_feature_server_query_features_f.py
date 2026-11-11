from typing import Literal

ArcgisFeatureServerQueryFeaturesF = Literal["json"]

ARCGIS_FEATURE_SERVER_QUERY_FEATURES_F_VALUES: set[
    ArcgisFeatureServerQueryFeaturesF
] = {
    "json",
}


def check_arcgis_feature_server_query_features_f(
    value: str,
) -> ArcgisFeatureServerQueryFeaturesF:
    if value in ARCGIS_FEATURE_SERVER_QUERY_FEATURES_F_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARCGIS_FEATURE_SERVER_QUERY_FEATURES_F_VALUES!r}"
    )
