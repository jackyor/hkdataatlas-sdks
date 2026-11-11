from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nine_day_forecast_weather_forecast_item_forecast_maxrh_type_2 import (
        NineDayForecastWeatherForecastItemForecastMaxrhType2,
    )
    from ..models.nine_day_forecast_weather_forecast_item_forecast_maxtemp_type_2 import (
        NineDayForecastWeatherForecastItemForecastMaxtempType2,
    )
    from ..models.nine_day_forecast_weather_forecast_item_forecast_minrh_type_2 import (
        NineDayForecastWeatherForecastItemForecastMinrhType2,
    )
    from ..models.nine_day_forecast_weather_forecast_item_forecast_mintemp_type_2 import (
        NineDayForecastWeatherForecastItemForecastMintempType2,
    )
    from ..models.temperature_measurement import TemperatureMeasurement


T = TypeVar("T", bound="NineDayForecastWeatherForecastItem")


@_attrs_define
class NineDayForecastWeatherForecastItem:
    """
    Attributes:
        forecast_icon (int | str | Unset): Forecast weather icon; see
            https://www.hko.gov.hk/textonly/v2/explain/wxicon_e.htm.
        psr (str | Unset): Probability of Significant Rain. Documented values include High, Medium High, Medium, Medium
            Low and Low; this list is not established as exhaustive.
        forecast_date (str | Unset): Forecast date, YYYYMMDD.
        forecast_maxrh (float | NineDayForecastWeatherForecastItemForecastMaxrhType2 | str | Unset): Forecast maximum
            relative humidity; the source does not specify its exact JSON wire type.
        forecast_maxtemp (float | NineDayForecastWeatherForecastItemForecastMaxtempType2 | str | Unset): Forecast
            maximum temperature; the source does not specify its exact JSON wire type.
        forecast_minrh (float | NineDayForecastWeatherForecastItemForecastMinrhType2 | str | Unset): Forecast minimum
            relative humidity; the source does not specify its exact JSON wire type.
        forecast_mintemp (float | NineDayForecastWeatherForecastItemForecastMintempType2 | str | Unset): Forecast
            minimum temperature; the source does not specify its exact JSON wire type.
        forecast_weather (str | Unset): Forecast weather.
        forecast_wind (str | Unset): Forecast wind.
        sea_temp (TemperatureMeasurement | Unset):
        soil_temp (list[TemperatureMeasurement] | Unset): Soil temperature measurements.
        week (str | Unset): Week.
    """

    forecast_icon: int | str | Unset = UNSET
    psr: str | Unset = UNSET
    forecast_date: str | Unset = UNSET
    forecast_maxrh: (
        float | NineDayForecastWeatherForecastItemForecastMaxrhType2 | str | Unset
    ) = UNSET
    forecast_maxtemp: (
        float | NineDayForecastWeatherForecastItemForecastMaxtempType2 | str | Unset
    ) = UNSET
    forecast_minrh: (
        float | NineDayForecastWeatherForecastItemForecastMinrhType2 | str | Unset
    ) = UNSET
    forecast_mintemp: (
        float | NineDayForecastWeatherForecastItemForecastMintempType2 | str | Unset
    ) = UNSET
    forecast_weather: str | Unset = UNSET
    forecast_wind: str | Unset = UNSET
    sea_temp: TemperatureMeasurement | Unset = UNSET
    soil_temp: list[TemperatureMeasurement] | Unset = UNSET
    week: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nine_day_forecast_weather_forecast_item_forecast_maxrh_type_2 import (
            NineDayForecastWeatherForecastItemForecastMaxrhType2,
        )
        from ..models.nine_day_forecast_weather_forecast_item_forecast_maxtemp_type_2 import (
            NineDayForecastWeatherForecastItemForecastMaxtempType2,
        )
        from ..models.nine_day_forecast_weather_forecast_item_forecast_minrh_type_2 import (
            NineDayForecastWeatherForecastItemForecastMinrhType2,
        )
        from ..models.nine_day_forecast_weather_forecast_item_forecast_mintemp_type_2 import (
            NineDayForecastWeatherForecastItemForecastMintempType2,
        )

        forecast_icon: int | str | Unset
        if isinstance(self.forecast_icon, Unset):
            forecast_icon = UNSET
        else:
            forecast_icon = self.forecast_icon

        psr = self.psr

        forecast_date = self.forecast_date

        forecast_maxrh: dict[str, Any] | float | str | Unset
        if isinstance(self.forecast_maxrh, Unset):
            forecast_maxrh = UNSET
        elif isinstance(
            self.forecast_maxrh, NineDayForecastWeatherForecastItemForecastMaxrhType2
        ):
            forecast_maxrh = self.forecast_maxrh.to_dict()
        else:
            forecast_maxrh = self.forecast_maxrh

        forecast_maxtemp: dict[str, Any] | float | str | Unset
        if isinstance(self.forecast_maxtemp, Unset):
            forecast_maxtemp = UNSET
        elif isinstance(
            self.forecast_maxtemp,
            NineDayForecastWeatherForecastItemForecastMaxtempType2,
        ):
            forecast_maxtemp = self.forecast_maxtemp.to_dict()
        else:
            forecast_maxtemp = self.forecast_maxtemp

        forecast_minrh: dict[str, Any] | float | str | Unset
        if isinstance(self.forecast_minrh, Unset):
            forecast_minrh = UNSET
        elif isinstance(
            self.forecast_minrh, NineDayForecastWeatherForecastItemForecastMinrhType2
        ):
            forecast_minrh = self.forecast_minrh.to_dict()
        else:
            forecast_minrh = self.forecast_minrh

        forecast_mintemp: dict[str, Any] | float | str | Unset
        if isinstance(self.forecast_mintemp, Unset):
            forecast_mintemp = UNSET
        elif isinstance(
            self.forecast_mintemp,
            NineDayForecastWeatherForecastItemForecastMintempType2,
        ):
            forecast_mintemp = self.forecast_mintemp.to_dict()
        else:
            forecast_mintemp = self.forecast_mintemp

        forecast_weather = self.forecast_weather

        forecast_wind = self.forecast_wind

        sea_temp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sea_temp, Unset):
            sea_temp = self.sea_temp.to_dict()

        soil_temp: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.soil_temp, Unset):
            soil_temp = []
            for soil_temp_item_data in self.soil_temp:
                soil_temp_item = soil_temp_item_data.to_dict()
                soil_temp.append(soil_temp_item)

        week = self.week

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if forecast_icon is not UNSET:
            field_dict["ForecastIcon"] = forecast_icon
        if psr is not UNSET:
            field_dict["PSR"] = psr
        if forecast_date is not UNSET:
            field_dict["forecastDate"] = forecast_date
        if forecast_maxrh is not UNSET:
            field_dict["forecastMaxrh"] = forecast_maxrh
        if forecast_maxtemp is not UNSET:
            field_dict["forecastMaxtemp"] = forecast_maxtemp
        if forecast_minrh is not UNSET:
            field_dict["forecastMinrh"] = forecast_minrh
        if forecast_mintemp is not UNSET:
            field_dict["forecastMintemp"] = forecast_mintemp
        if forecast_weather is not UNSET:
            field_dict["forecastWeather"] = forecast_weather
        if forecast_wind is not UNSET:
            field_dict["forecastWind"] = forecast_wind
        if sea_temp is not UNSET:
            field_dict["seaTemp"] = sea_temp
        if soil_temp is not UNSET:
            field_dict["soilTemp"] = soil_temp
        if week is not UNSET:
            field_dict["week"] = week

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.nine_day_forecast_weather_forecast_item_forecast_maxrh_type_2 import (
            NineDayForecastWeatherForecastItemForecastMaxrhType2,
        )
        from ..models.nine_day_forecast_weather_forecast_item_forecast_maxtemp_type_2 import (
            NineDayForecastWeatherForecastItemForecastMaxtempType2,
        )
        from ..models.nine_day_forecast_weather_forecast_item_forecast_minrh_type_2 import (
            NineDayForecastWeatherForecastItemForecastMinrhType2,
        )
        from ..models.nine_day_forecast_weather_forecast_item_forecast_mintemp_type_2 import (
            NineDayForecastWeatherForecastItemForecastMintempType2,
        )
        from ..models.temperature_measurement import TemperatureMeasurement

        d = dict(src_dict)

        def _parse_forecast_icon(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        forecast_icon = _parse_forecast_icon(d.pop("ForecastIcon", UNSET))

        psr = d.pop("PSR", UNSET)

        forecast_date = d.pop("forecastDate", UNSET)

        def _parse_forecast_maxrh(
            data: object,
        ) -> float | NineDayForecastWeatherForecastItemForecastMaxrhType2 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                forecast_maxrh_type_2 = (
                    NineDayForecastWeatherForecastItemForecastMaxrhType2.from_dict(data)
                )

                return forecast_maxrh_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                float
                | NineDayForecastWeatherForecastItemForecastMaxrhType2
                | str
                | Unset,
                data,
            )

        forecast_maxrh = _parse_forecast_maxrh(d.pop("forecastMaxrh", UNSET))

        def _parse_forecast_maxtemp(
            data: object,
        ) -> (
            float | NineDayForecastWeatherForecastItemForecastMaxtempType2 | str | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                forecast_maxtemp_type_2 = (
                    NineDayForecastWeatherForecastItemForecastMaxtempType2.from_dict(
                        data
                    )
                )

                return forecast_maxtemp_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                float
                | NineDayForecastWeatherForecastItemForecastMaxtempType2
                | str
                | Unset,
                data,
            )

        forecast_maxtemp = _parse_forecast_maxtemp(d.pop("forecastMaxtemp", UNSET))

        def _parse_forecast_minrh(
            data: object,
        ) -> float | NineDayForecastWeatherForecastItemForecastMinrhType2 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                forecast_minrh_type_2 = (
                    NineDayForecastWeatherForecastItemForecastMinrhType2.from_dict(data)
                )

                return forecast_minrh_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                float
                | NineDayForecastWeatherForecastItemForecastMinrhType2
                | str
                | Unset,
                data,
            )

        forecast_minrh = _parse_forecast_minrh(d.pop("forecastMinrh", UNSET))

        def _parse_forecast_mintemp(
            data: object,
        ) -> (
            float | NineDayForecastWeatherForecastItemForecastMintempType2 | str | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                forecast_mintemp_type_2 = (
                    NineDayForecastWeatherForecastItemForecastMintempType2.from_dict(
                        data
                    )
                )

                return forecast_mintemp_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                float
                | NineDayForecastWeatherForecastItemForecastMintempType2
                | str
                | Unset,
                data,
            )

        forecast_mintemp = _parse_forecast_mintemp(d.pop("forecastMintemp", UNSET))

        forecast_weather = d.pop("forecastWeather", UNSET)

        forecast_wind = d.pop("forecastWind", UNSET)

        _sea_temp = d.pop("seaTemp", UNSET)
        sea_temp: TemperatureMeasurement | Unset
        if isinstance(_sea_temp, Unset):
            sea_temp = UNSET
        else:
            sea_temp = TemperatureMeasurement.from_dict(_sea_temp)

        _soil_temp = d.pop("soilTemp", UNSET)
        soil_temp: list[TemperatureMeasurement] | Unset = UNSET
        if _soil_temp is not UNSET:
            soil_temp = []
            for soil_temp_item_data in _soil_temp:
                soil_temp_item = TemperatureMeasurement.from_dict(soil_temp_item_data)

                soil_temp.append(soil_temp_item)

        week = d.pop("week", UNSET)

        nine_day_forecast_weather_forecast_item = cls(
            forecast_icon=forecast_icon,
            psr=psr,
            forecast_date=forecast_date,
            forecast_maxrh=forecast_maxrh,
            forecast_maxtemp=forecast_maxtemp,
            forecast_minrh=forecast_minrh,
            forecast_mintemp=forecast_mintemp,
            forecast_weather=forecast_weather,
            forecast_wind=forecast_wind,
            sea_temp=sea_temp,
            soil_temp=soil_temp,
            week=week,
        )

        nine_day_forecast_weather_forecast_item.additional_properties = d
        return nine_day_forecast_weather_forecast_item

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
