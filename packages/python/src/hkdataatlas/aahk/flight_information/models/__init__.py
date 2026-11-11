"""Contains all the data models used in inputs/outputs"""

from .get_past_flight_information_lang import GetPastFlightInformationLang
from .observed_day_group import ObservedDayGroup
from .observed_flight_number import ObservedFlightNumber
from .observed_flight_record import ObservedFlightRecord

__all__ = (
    "GetPastFlightInformationLang",
    "ObservedDayGroup",
    "ObservedFlightNumber",
    "ObservedFlightRecord",
)
