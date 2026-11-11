from typing import Literal

WfsMapServerGetFeatureOutputFormat = Literal[
    "application/gml+xml; version=3.2",
    "application/vnd.google-earth.kml xml",
    "application/vnd.google-earth.kml+xml",
    "application/vnd.google-earth.kmz",
    "CSV",
    "CSV+GZIP",
    "CSV+ZIP",
    "ESRIGEOJSON",
    "ESRIGEOJSON+GZIP",
    "ESRIGEOJSON+ZIP",
    "GEOJSON",
    "GEOJSON+GZIP",
    "GEOJSON+ZIP",
    "Geopackage",
    "Geopackage+ZIP",
    "GML2",
    "GML2+GZIP",
    "GML2+ZIP",
    "GML3",
    "GML3+GZIP",
    "GML3+ZIP",
    "GML32",
    "GML32+GZIP",
    "GML32+ZIP",
    "KML",
    "KMZ",
    "SHAPE+ZIP",
    "text/xml; subtype=gml/2.1.2",
    "text/xml; subtype=gml/3.1.1",
]

WFS_MAP_SERVER_GET_FEATURE_OUTPUT_FORMAT_VALUES: set[
    WfsMapServerGetFeatureOutputFormat
] = {
    "application/gml+xml; version=3.2",
    "application/vnd.google-earth.kml xml",
    "application/vnd.google-earth.kml+xml",
    "application/vnd.google-earth.kmz",
    "CSV",
    "CSV+GZIP",
    "CSV+ZIP",
    "ESRIGEOJSON",
    "ESRIGEOJSON+GZIP",
    "ESRIGEOJSON+ZIP",
    "GEOJSON",
    "GEOJSON+GZIP",
    "GEOJSON+ZIP",
    "Geopackage",
    "Geopackage+ZIP",
    "GML2",
    "GML2+GZIP",
    "GML2+ZIP",
    "GML3",
    "GML3+GZIP",
    "GML3+ZIP",
    "GML32",
    "GML32+GZIP",
    "GML32+ZIP",
    "KML",
    "KMZ",
    "SHAPE+ZIP",
    "text/xml; subtype=gml/2.1.2",
    "text/xml; subtype=gml/3.1.1",
}


def check_wfs_map_server_get_feature_output_format(
    value: str,
) -> WfsMapServerGetFeatureOutputFormat:
    if value in WFS_MAP_SERVER_GET_FEATURE_OUTPUT_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WFS_MAP_SERVER_GET_FEATURE_OUTPUT_FORMAT_VALUES!r}"
    )
