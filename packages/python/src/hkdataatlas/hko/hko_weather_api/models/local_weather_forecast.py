from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalWeatherForecast")


@_attrs_define
class LocalWeatherForecast:
    """Local Weather Forecast (flw).

    Attributes:
        fire_danger_warning (str | Unset): Fire Danger Warning Message.
        forecast_desc (str | Unset): Forecast Description.
        forecast_period (str | Unset): Forecast Period.
        general_situation (str | Unset): General Situation.
        outlook (str | Unset): Outlook.
        tc_info (str | Unset): Tropical Cyclone Information; exact structure is not detailed.
        update_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
    """

    fire_danger_warning: str | Unset = UNSET
    forecast_desc: str | Unset = UNSET
    forecast_period: str | Unset = UNSET
    general_situation: str | Unset = UNSET
    outlook: str | Unset = UNSET
    tc_info: str | Unset = UNSET
    update_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fire_danger_warning = self.fire_danger_warning

        forecast_desc = self.forecast_desc

        forecast_period = self.forecast_period

        general_situation = self.general_situation

        outlook = self.outlook

        tc_info = self.tc_info

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fire_danger_warning is not UNSET:
            field_dict["fireDangerWarning"] = fire_danger_warning
        if forecast_desc is not UNSET:
            field_dict["forecastDesc"] = forecast_desc
        if forecast_period is not UNSET:
            field_dict["forecastPeriod"] = forecast_period
        if general_situation is not UNSET:
            field_dict["generalSituation"] = general_situation
        if outlook is not UNSET:
            field_dict["outlook"] = outlook
        if tc_info is not UNSET:
            field_dict["tcInfo"] = tc_info
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fire_danger_warning = d.pop("fireDangerWarning", UNSET)

        forecast_desc = d.pop("forecastDesc", UNSET)

        forecast_period = d.pop("forecastPeriod", UNSET)

        general_situation = d.pop("generalSituation", UNSET)

        outlook = d.pop("outlook", UNSET)

        tc_info = d.pop("tcInfo", UNSET)

        update_time = d.pop("updateTime", UNSET)

        local_weather_forecast = cls(
            fire_danger_warning=fire_danger_warning,
            forecast_desc=forecast_desc,
            forecast_period=forecast_period,
            general_situation=general_situation,
            outlook=outlook,
            tc_info=tc_info,
            update_time=update_time,
        )

        local_weather_forecast.additional_properties = d
        return local_weather_forecast

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
