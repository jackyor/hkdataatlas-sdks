"""Contains all the data models used in inputs/outputs"""

from .get_map_presentation_style_lang import GetMapPresentationStyleLang
from .get_map_presentation_style_sr import GetMapPresentationStyleSr
from .get_vector_map_label_tile_lang import GetVectorMapLabelTileLang
from .get_vector_map_label_tile_sr import GetVectorMapLabelTileSr

__all__ = (
    "GetMapPresentationStyleLang",
    "GetMapPresentationStyleSr",
    "GetVectorMapLabelTileLang",
    "GetVectorMapLabelTileSr",
)
