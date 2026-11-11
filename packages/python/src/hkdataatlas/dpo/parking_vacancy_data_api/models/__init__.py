"""Contains all the data models used in inputs/outputs"""

from .carpark_info import CarparkInfo
from .carpark_info_lang import CarparkInfoLang
from .carpark_vacancy import CarparkVacancy
from .day_night_park import DayNightPark
from .day_night_park_covered import DayNightParkCovered
from .day_night_park_type import DayNightParkType
from .day_night_park_valid_until import DayNightParkValidUntil
from .get_carpark_info_vacancy_data import GetCarparkInfoVacancyData
from .get_carpark_info_vacancy_lang import GetCarparkInfoVacancyLang
from .get_carpark_info_vacancy_response_200 import GetCarparkInfoVacancyResponse200
from .grace_period import GracePeriod
from .height_limit import HeightLimit
from .hourly_charge import HourlyCharge
from .hourly_charge_covered import HourlyChargeCovered
from .hourly_charge_type import HourlyChargeType
from .monthly_charge import MonthlyCharge
from .monthly_charge_covered import MonthlyChargeCovered
from .monthly_charge_reserved import MonthlyChargeReserved
from .monthly_charge_type import MonthlyChargeType
from .opening_hour import OpeningHour
from .privilege import Privilege
from .rendition_urls import RenditionUrls
from .time_range import TimeRange
from .unloading import Unloading
from .unloading_type import UnloadingType
from .usage_threshold import UsageThreshold
from .vacancy_record import VacancyRecord
from .vacancy_record_category import VacancyRecordCategory
from .vacancy_record_vacancy_type import VacancyRecordVacancyType
from .vehicle_information import VehicleInformation
from .weekdays_item import WeekdaysItem

__all__ = (
    "CarparkInfo",
    "CarparkInfoLang",
    "CarparkVacancy",
    "DayNightPark",
    "DayNightParkCovered",
    "DayNightParkType",
    "DayNightParkValidUntil",
    "GetCarparkInfoVacancyData",
    "GetCarparkInfoVacancyLang",
    "GetCarparkInfoVacancyResponse200",
    "GracePeriod",
    "HeightLimit",
    "HourlyCharge",
    "HourlyChargeCovered",
    "HourlyChargeType",
    "MonthlyCharge",
    "MonthlyChargeCovered",
    "MonthlyChargeReserved",
    "MonthlyChargeType",
    "OpeningHour",
    "Privilege",
    "RenditionUrls",
    "TimeRange",
    "Unloading",
    "UnloadingType",
    "UsageThreshold",
    "VacancyRecord",
    "VacancyRecordCategory",
    "VacancyRecordVacancyType",
    "VehicleInformation",
    "WeekdaysItem",
)
