from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nine_day_forecast_weather_forecast_item import (
        NineDayForecastWeatherForecastItem,
    )


T = TypeVar("T", bound="NineDayForecast")


@_attrs_define
class NineDayForecast:
    """9-day Weather Forecast (fnd).

    Attributes:
        weather_forecast (list[NineDayForecastWeatherForecastItem] | Unset): List of forecast entries.
    """

    weather_forecast: list[NineDayForecastWeatherForecastItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weather_forecast: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.weather_forecast, Unset):
            weather_forecast = []
            for weather_forecast_item_data in self.weather_forecast:
                weather_forecast_item = weather_forecast_item_data.to_dict()
                weather_forecast.append(weather_forecast_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weather_forecast is not UNSET:
            field_dict["weatherForecast"] = weather_forecast

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.nine_day_forecast_weather_forecast_item import (
            NineDayForecastWeatherForecastItem,
        )

        d = dict(src_dict)
        _weather_forecast = d.pop("weatherForecast", UNSET)
        weather_forecast: list[NineDayForecastWeatherForecastItem] | Unset = UNSET
        if _weather_forecast is not UNSET:
            weather_forecast = []
            for weather_forecast_item_data in _weather_forecast:
                weather_forecast_item = NineDayForecastWeatherForecastItem.from_dict(
                    weather_forecast_item_data
                )

                weather_forecast.append(weather_forecast_item)

        nine_day_forecast = cls(
            weather_forecast=weather_forecast,
        )

        nine_day_forecast.additional_properties = d
        return nine_day_forecast

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
