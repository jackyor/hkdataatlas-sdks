from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_weather_report_lightning import CurrentWeatherReportLightning
    from ..models.current_weather_report_mintemp_from_00_to_09_type_2 import (
        CurrentWeatherReportMintempFrom00To09Type2,
    )
    from ..models.current_weather_report_rainfall import CurrentWeatherReportRainfall
    from ..models.current_weather_report_rainfall_from_00_to_12_type_2 import (
        CurrentWeatherReportRainfallFrom00To12Type2,
    )
    from ..models.current_weather_report_rainfall_january_to_last_month_type_2 import (
        CurrentWeatherReportRainfallJanuaryToLastMonthType2,
    )
    from ..models.current_weather_report_rainfall_last_month_type_2 import (
        CurrentWeatherReportRainfallLastMonthType2,
    )
    from ..models.current_weather_report_rainstorm_reminder_type_1 import (
        CurrentWeatherReportRainstormReminderType1,
    )
    from ..models.current_weather_report_uvindex import CurrentWeatherReportUvindex
    from ..models.weather_observation import WeatherObservation


T = TypeVar("T", bound="CurrentWeatherReport")


@_attrs_define
class CurrentWeatherReport:
    """Current Weather Report (rhrread). Parameters may be missing when values are null or unavailable; UV index may be an
    empty string when no data is available.

        Attributes:
            humidity (list[WeatherObservation] | Unset): Humidity observations.
            icon (list[int] | Unset): Weather icon list; see https://www.hko.gov.hk/textonly/v2/explain/wxicon_e.htm.
            icon_update_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00
                offset.
            lightning (CurrentWeatherReportLightning | Unset):
            mintemp_from_00_to_09 (CurrentWeatherReportMintempFrom00To09Type2 | float | str | Unset): Minimum temperature
                from midnight to 9 am; exact JSON structure is not specified.
            rainfall (CurrentWeatherReportRainfall | Unset):
            rainfall_from_00_to_12 (CurrentWeatherReportRainfallFrom00To12Type2 | float | str | Unset): Accumulated rainfall
                at HKO from midnight to noon; exact JSON structure is not specified.
            rainfall_january_to_last_month (CurrentWeatherReportRainfallJanuaryToLastMonthType2 | float | str | Unset):
                Accumulated rainfall from January to last month; exact JSON structure is not specified.
            rainfall_last_month (CurrentWeatherReportRainfallLastMonthType2 | float | str | Unset): Rainfall in last month;
                exact JSON structure is not specified.
            rainstorm_reminder (CurrentWeatherReportRainstormReminderType1 | list[Any] | str | Unset): Rainstorm Reminder;
                exact JSON structure is not specified.
            special_wx_tips (list[str] | Unset): Special Weather Tips.
            tcmessage (list[str] | Unset): Message of tropical cyclone position.
            temperature (list[WeatherObservation] | Unset): Temperature observations.
            uvindex (CurrentWeatherReportUvindex | Unset):
            warning_message (list[str] | Unset): Warning messages; an empty string is returned if no warning-message data is
                available.
    """

    humidity: list[WeatherObservation] | Unset = UNSET
    icon: list[int] | Unset = UNSET
    icon_update_time: str | Unset = UNSET
    lightning: CurrentWeatherReportLightning | Unset = UNSET
    mintemp_from_00_to_09: (
        CurrentWeatherReportMintempFrom00To09Type2 | float | str | Unset
    ) = UNSET
    rainfall: CurrentWeatherReportRainfall | Unset = UNSET
    rainfall_from_00_to_12: (
        CurrentWeatherReportRainfallFrom00To12Type2 | float | str | Unset
    ) = UNSET
    rainfall_january_to_last_month: (
        CurrentWeatherReportRainfallJanuaryToLastMonthType2 | float | str | Unset
    ) = UNSET
    rainfall_last_month: (
        CurrentWeatherReportRainfallLastMonthType2 | float | str | Unset
    ) = UNSET
    rainstorm_reminder: (
        CurrentWeatherReportRainstormReminderType1 | list[Any] | str | Unset
    ) = UNSET
    special_wx_tips: list[str] | Unset = UNSET
    tcmessage: list[str] | Unset = UNSET
    temperature: list[WeatherObservation] | Unset = UNSET
    uvindex: CurrentWeatherReportUvindex | Unset = UNSET
    warning_message: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.current_weather_report_mintemp_from_00_to_09_type_2 import (
            CurrentWeatherReportMintempFrom00To09Type2,
        )
        from ..models.current_weather_report_rainfall_from_00_to_12_type_2 import (
            CurrentWeatherReportRainfallFrom00To12Type2,
        )
        from ..models.current_weather_report_rainfall_january_to_last_month_type_2 import (
            CurrentWeatherReportRainfallJanuaryToLastMonthType2,
        )
        from ..models.current_weather_report_rainfall_last_month_type_2 import (
            CurrentWeatherReportRainfallLastMonthType2,
        )
        from ..models.current_weather_report_rainstorm_reminder_type_1 import (
            CurrentWeatherReportRainstormReminderType1,
        )

        humidity: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.humidity, Unset):
            humidity = []
            for humidity_item_data in self.humidity:
                humidity_item = humidity_item_data.to_dict()
                humidity.append(humidity_item)

        icon: list[int] | Unset = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon

        icon_update_time = self.icon_update_time

        lightning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lightning, Unset):
            lightning = self.lightning.to_dict()

        mintemp_from_00_to_09: dict[str, Any] | float | str | Unset
        if isinstance(self.mintemp_from_00_to_09, Unset):
            mintemp_from_00_to_09 = UNSET
        elif isinstance(
            self.mintemp_from_00_to_09, CurrentWeatherReportMintempFrom00To09Type2
        ):
            mintemp_from_00_to_09 = self.mintemp_from_00_to_09.to_dict()
        else:
            mintemp_from_00_to_09 = self.mintemp_from_00_to_09

        rainfall: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rainfall, Unset):
            rainfall = self.rainfall.to_dict()

        rainfall_from_00_to_12: dict[str, Any] | float | str | Unset
        if isinstance(self.rainfall_from_00_to_12, Unset):
            rainfall_from_00_to_12 = UNSET
        elif isinstance(
            self.rainfall_from_00_to_12, CurrentWeatherReportRainfallFrom00To12Type2
        ):
            rainfall_from_00_to_12 = self.rainfall_from_00_to_12.to_dict()
        else:
            rainfall_from_00_to_12 = self.rainfall_from_00_to_12

        rainfall_january_to_last_month: dict[str, Any] | float | str | Unset
        if isinstance(self.rainfall_january_to_last_month, Unset):
            rainfall_january_to_last_month = UNSET
        elif isinstance(
            self.rainfall_january_to_last_month,
            CurrentWeatherReportRainfallJanuaryToLastMonthType2,
        ):
            rainfall_january_to_last_month = (
                self.rainfall_january_to_last_month.to_dict()
            )
        else:
            rainfall_january_to_last_month = self.rainfall_january_to_last_month

        rainfall_last_month: dict[str, Any] | float | str | Unset
        if isinstance(self.rainfall_last_month, Unset):
            rainfall_last_month = UNSET
        elif isinstance(
            self.rainfall_last_month, CurrentWeatherReportRainfallLastMonthType2
        ):
            rainfall_last_month = self.rainfall_last_month.to_dict()
        else:
            rainfall_last_month = self.rainfall_last_month

        rainstorm_reminder: dict[str, Any] | list[Any] | str | Unset
        if isinstance(self.rainstorm_reminder, Unset):
            rainstorm_reminder = UNSET
        elif isinstance(
            self.rainstorm_reminder, CurrentWeatherReportRainstormReminderType1
        ):
            rainstorm_reminder = self.rainstorm_reminder.to_dict()
        elif isinstance(self.rainstorm_reminder, list):
            rainstorm_reminder = self.rainstorm_reminder

        else:
            rainstorm_reminder = self.rainstorm_reminder

        special_wx_tips: list[str] | Unset = UNSET
        if not isinstance(self.special_wx_tips, Unset):
            special_wx_tips = self.special_wx_tips

        tcmessage: list[str] | Unset = UNSET
        if not isinstance(self.tcmessage, Unset):
            tcmessage = self.tcmessage

        temperature: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.temperature, Unset):
            temperature = []
            for temperature_item_data in self.temperature:
                temperature_item = temperature_item_data.to_dict()
                temperature.append(temperature_item)

        uvindex: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uvindex, Unset):
            uvindex = self.uvindex.to_dict()

        warning_message: list[str] | Unset = UNSET
        if not isinstance(self.warning_message, Unset):
            warning_message = self.warning_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if humidity is not UNSET:
            field_dict["humidity"] = humidity
        if icon is not UNSET:
            field_dict["icon"] = icon
        if icon_update_time is not UNSET:
            field_dict["iconUpdateTime"] = icon_update_time
        if lightning is not UNSET:
            field_dict["lightning"] = lightning
        if mintemp_from_00_to_09 is not UNSET:
            field_dict["mintempFrom00To09"] = mintemp_from_00_to_09
        if rainfall is not UNSET:
            field_dict["rainfall"] = rainfall
        if rainfall_from_00_to_12 is not UNSET:
            field_dict["rainfallFrom00To12"] = rainfall_from_00_to_12
        if rainfall_january_to_last_month is not UNSET:
            field_dict["rainfallJanuaryToLastMonth"] = rainfall_january_to_last_month
        if rainfall_last_month is not UNSET:
            field_dict["rainfallLastMonth"] = rainfall_last_month
        if rainstorm_reminder is not UNSET:
            field_dict["rainstormReminder"] = rainstorm_reminder
        if special_wx_tips is not UNSET:
            field_dict["specialWxTips"] = special_wx_tips
        if tcmessage is not UNSET:
            field_dict["tcmessage"] = tcmessage
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if uvindex is not UNSET:
            field_dict["uvindex"] = uvindex
        if warning_message is not UNSET:
            field_dict["warningMessage"] = warning_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.current_weather_report_lightning import (
            CurrentWeatherReportLightning,
        )
        from ..models.current_weather_report_mintemp_from_00_to_09_type_2 import (
            CurrentWeatherReportMintempFrom00To09Type2,
        )
        from ..models.current_weather_report_rainfall import (
            CurrentWeatherReportRainfall,
        )
        from ..models.current_weather_report_rainfall_from_00_to_12_type_2 import (
            CurrentWeatherReportRainfallFrom00To12Type2,
        )
        from ..models.current_weather_report_rainfall_january_to_last_month_type_2 import (
            CurrentWeatherReportRainfallJanuaryToLastMonthType2,
        )
        from ..models.current_weather_report_rainfall_last_month_type_2 import (
            CurrentWeatherReportRainfallLastMonthType2,
        )
        from ..models.current_weather_report_rainstorm_reminder_type_1 import (
            CurrentWeatherReportRainstormReminderType1,
        )
        from ..models.current_weather_report_uvindex import CurrentWeatherReportUvindex
        from ..models.weather_observation import WeatherObservation

        d = dict(src_dict)
        _humidity = d.pop("humidity", UNSET)
        humidity: list[WeatherObservation] | Unset = UNSET
        if _humidity is not UNSET:
            humidity = []
            for humidity_item_data in _humidity:
                humidity_item = WeatherObservation.from_dict(humidity_item_data)

                humidity.append(humidity_item)

        icon = cast(list[int], d.pop("icon", UNSET))

        icon_update_time = d.pop("iconUpdateTime", UNSET)

        _lightning = d.pop("lightning", UNSET)
        lightning: CurrentWeatherReportLightning | Unset
        if isinstance(_lightning, Unset):
            lightning = UNSET
        else:
            lightning = CurrentWeatherReportLightning.from_dict(_lightning)

        def _parse_mintemp_from_00_to_09(
            data: object,
        ) -> CurrentWeatherReportMintempFrom00To09Type2 | float | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mintemp_from_00_to_09_type_2 = (
                    CurrentWeatherReportMintempFrom00To09Type2.from_dict(data)
                )

                return mintemp_from_00_to_09_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CurrentWeatherReportMintempFrom00To09Type2 | float | str | Unset, data
            )

        mintemp_from_00_to_09 = _parse_mintemp_from_00_to_09(
            d.pop("mintempFrom00To09", UNSET)
        )

        _rainfall = d.pop("rainfall", UNSET)
        rainfall: CurrentWeatherReportRainfall | Unset
        if isinstance(_rainfall, Unset):
            rainfall = UNSET
        else:
            rainfall = CurrentWeatherReportRainfall.from_dict(_rainfall)

        def _parse_rainfall_from_00_to_12(
            data: object,
        ) -> CurrentWeatherReportRainfallFrom00To12Type2 | float | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rainfall_from_00_to_12_type_2 = (
                    CurrentWeatherReportRainfallFrom00To12Type2.from_dict(data)
                )

                return rainfall_from_00_to_12_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CurrentWeatherReportRainfallFrom00To12Type2 | float | str | Unset, data
            )

        rainfall_from_00_to_12 = _parse_rainfall_from_00_to_12(
            d.pop("rainfallFrom00To12", UNSET)
        )

        def _parse_rainfall_january_to_last_month(
            data: object,
        ) -> CurrentWeatherReportRainfallJanuaryToLastMonthType2 | float | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rainfall_january_to_last_month_type_2 = (
                    CurrentWeatherReportRainfallJanuaryToLastMonthType2.from_dict(data)
                )

                return rainfall_january_to_last_month_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CurrentWeatherReportRainfallJanuaryToLastMonthType2
                | float
                | str
                | Unset,
                data,
            )

        rainfall_january_to_last_month = _parse_rainfall_january_to_last_month(
            d.pop("rainfallJanuaryToLastMonth", UNSET)
        )

        def _parse_rainfall_last_month(
            data: object,
        ) -> CurrentWeatherReportRainfallLastMonthType2 | float | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rainfall_last_month_type_2 = (
                    CurrentWeatherReportRainfallLastMonthType2.from_dict(data)
                )

                return rainfall_last_month_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CurrentWeatherReportRainfallLastMonthType2 | float | str | Unset, data
            )

        rainfall_last_month = _parse_rainfall_last_month(
            d.pop("rainfallLastMonth", UNSET)
        )

        def _parse_rainstorm_reminder(
            data: object,
        ) -> CurrentWeatherReportRainstormReminderType1 | list[Any] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rainstorm_reminder_type_1 = (
                    CurrentWeatherReportRainstormReminderType1.from_dict(data)
                )

                return rainstorm_reminder_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rainstorm_reminder_type_2 = cast(list[Any], data)

                return rainstorm_reminder_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CurrentWeatherReportRainstormReminderType1 | list[Any] | str | Unset,
                data,
            )

        rainstorm_reminder = _parse_rainstorm_reminder(
            d.pop("rainstormReminder", UNSET)
        )

        special_wx_tips = cast(list[str], d.pop("specialWxTips", UNSET))

        tcmessage = cast(list[str], d.pop("tcmessage", UNSET))

        _temperature = d.pop("temperature", UNSET)
        temperature: list[WeatherObservation] | Unset = UNSET
        if _temperature is not UNSET:
            temperature = []
            for temperature_item_data in _temperature:
                temperature_item = WeatherObservation.from_dict(temperature_item_data)

                temperature.append(temperature_item)

        _uvindex = d.pop("uvindex", UNSET)
        uvindex: CurrentWeatherReportUvindex | Unset
        if isinstance(_uvindex, Unset):
            uvindex = UNSET
        else:
            uvindex = CurrentWeatherReportUvindex.from_dict(_uvindex)

        warning_message = cast(list[str], d.pop("warningMessage", UNSET))

        current_weather_report = cls(
            humidity=humidity,
            icon=icon,
            icon_update_time=icon_update_time,
            lightning=lightning,
            mintemp_from_00_to_09=mintemp_from_00_to_09,
            rainfall=rainfall,
            rainfall_from_00_to_12=rainfall_from_00_to_12,
            rainfall_january_to_last_month=rainfall_january_to_last_month,
            rainfall_last_month=rainfall_last_month,
            rainstorm_reminder=rainstorm_reminder,
            special_wx_tips=special_wx_tips,
            tcmessage=tcmessage,
            temperature=temperature,
            uvindex=uvindex,
            warning_message=warning_message,
        )

        current_weather_report.additional_properties = d
        return current_weather_report

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
