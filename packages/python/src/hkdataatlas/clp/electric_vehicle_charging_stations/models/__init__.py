"""Contains all the data models used in inputs/outputs"""

from .charger import Charger
from .data import Data
from .geo_location_result import GeoLocationResult
from .sample_response import SampleResponse

__all__ = (
    "Charger",
    "Data",
    "GeoLocationResult",
    "SampleResponse",
)
