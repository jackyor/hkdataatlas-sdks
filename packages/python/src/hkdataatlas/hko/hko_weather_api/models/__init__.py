"""Contains all the data models used in inputs/outputs"""

from .current_weather_report import CurrentWeatherReport
from .current_weather_report_lightning import CurrentWeatherReportLightning
from .current_weather_report_mintemp_from_00_to_09_type_2 import (
    CurrentWeatherReportMintempFrom00To09Type2,
)
from .current_weather_report_rainfall import CurrentWeatherReportRainfall
from .current_weather_report_rainfall_from_00_to_12_type_2 import (
    CurrentWeatherReportRainfallFrom00To12Type2,
)
from .current_weather_report_rainfall_january_to_last_month_type_2 import (
    CurrentWeatherReportRainfallJanuaryToLastMonthType2,
)
from .current_weather_report_rainfall_last_month_type_2 import (
    CurrentWeatherReportRainfallLastMonthType2,
)
from .current_weather_report_rainfall_place_item import (
    CurrentWeatherReportRainfallPlaceItem,
)
from .current_weather_report_rainstorm_reminder_type_1 import (
    CurrentWeatherReportRainstormReminderType1,
)
from .current_weather_report_uvindex import CurrentWeatherReportUvindex
from .felt_earth_tremor_report import FeltEarthTremorReport
from .get_climate_weather_open_data_data_type import GetClimateWeatherOpenDataDataType
from .get_climate_weather_open_data_lang import GetClimateWeatherOpenDataLang
from .get_climate_weather_open_data_rformat import GetClimateWeatherOpenDataRformat
from .get_earthquake_information_data_type import GetEarthquakeInformationDataType
from .get_earthquake_information_lang import GetEarthquakeInformationLang
from .get_hourly_rainfall_lang import GetHourlyRainfallLang
from .get_weather_information_data_type import GetWeatherInformationDataType
from .get_weather_information_lang import GetWeatherInformationLang
from .hourly_rainfall_report import HourlyRainfallReport
from .hourly_rainfall_station import HourlyRainfallStation
from .local_weather_forecast import LocalWeatherForecast
from .lunar_date_conversion import LunarDateConversion
from .nine_day_forecast import NineDayForecast
from .nine_day_forecast_weather_forecast_item import NineDayForecastWeatherForecastItem
from .nine_day_forecast_weather_forecast_item_forecast_maxrh_type_2 import (
    NineDayForecastWeatherForecastItemForecastMaxrhType2,
)
from .nine_day_forecast_weather_forecast_item_forecast_maxtemp_type_2 import (
    NineDayForecastWeatherForecastItemForecastMaxtempType2,
)
from .nine_day_forecast_weather_forecast_item_forecast_minrh_type_2 import (
    NineDayForecastWeatherForecastItemForecastMinrhType2,
)
from .nine_day_forecast_weather_forecast_item_forecast_mintemp_type_2 import (
    NineDayForecastWeatherForecastItemForecastMintempType2,
)
from .quick_earthquake_message import QuickEarthquakeMessage
from .special_weather_tips import SpecialWeatherTips
from .special_weather_tips_swt_item import SpecialWeatherTipsSwtItem
from .tabular_open_data import TabularOpenData
from .temperature_measurement import TemperatureMeasurement
from .warning_information_entry import WarningInformationEntry
from .warning_summary_entry import WarningSummaryEntry
from .weather_observation import WeatherObservation
from .weather_radiation_report import WeatherRadiationReport
from .weather_radiation_report_additional_property_type_2 import (
    WeatherRadiationReportAdditionalPropertyType2,
)
from .weather_warning_information import WeatherWarningInformation
from .weather_warning_summary import WeatherWarningSummary

__all__ = (
    "CurrentWeatherReport",
    "CurrentWeatherReportLightning",
    "CurrentWeatherReportMintempFrom00To09Type2",
    "CurrentWeatherReportRainfall",
    "CurrentWeatherReportRainfallFrom00To12Type2",
    "CurrentWeatherReportRainfallJanuaryToLastMonthType2",
    "CurrentWeatherReportRainfallLastMonthType2",
    "CurrentWeatherReportRainfallPlaceItem",
    "CurrentWeatherReportRainstormReminderType1",
    "CurrentWeatherReportUvindex",
    "FeltEarthTremorReport",
    "GetClimateWeatherOpenDataDataType",
    "GetClimateWeatherOpenDataLang",
    "GetClimateWeatherOpenDataRformat",
    "GetEarthquakeInformationDataType",
    "GetEarthquakeInformationLang",
    "GetHourlyRainfallLang",
    "GetWeatherInformationDataType",
    "GetWeatherInformationLang",
    "HourlyRainfallReport",
    "HourlyRainfallStation",
    "LocalWeatherForecast",
    "LunarDateConversion",
    "NineDayForecast",
    "NineDayForecastWeatherForecastItem",
    "NineDayForecastWeatherForecastItemForecastMaxrhType2",
    "NineDayForecastWeatherForecastItemForecastMaxtempType2",
    "NineDayForecastWeatherForecastItemForecastMinrhType2",
    "NineDayForecastWeatherForecastItemForecastMintempType2",
    "QuickEarthquakeMessage",
    "SpecialWeatherTips",
    "SpecialWeatherTipsSwtItem",
    "TabularOpenData",
    "TemperatureMeasurement",
    "WarningInformationEntry",
    "WarningSummaryEntry",
    "WeatherObservation",
    "WeatherRadiationReport",
    "WeatherRadiationReportAdditionalPropertyType2",
    "WeatherWarningInformation",
    "WeatherWarningSummary",
)
