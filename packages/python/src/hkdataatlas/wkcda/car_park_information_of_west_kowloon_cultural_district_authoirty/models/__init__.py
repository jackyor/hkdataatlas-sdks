"""Contains all the data models used in inputs/outputs"""

from .car_park import CarPark
from .car_park_response import CarParkResponse
from .localized_text import LocalizedText
from .vacancy import Vacancy

__all__ = (
    "CarPark",
    "CarParkResponse",
    "LocalizedText",
    "Vacancy",
)
