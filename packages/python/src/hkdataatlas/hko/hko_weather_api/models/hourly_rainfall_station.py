from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HourlyRainfallStation")


@_attrs_define
class HourlyRainfallStation:
    """
    Attributes:
        automatic_weather_station (str | Unset): Automatic weather station name.
        automatic_weather_station_id (str | Unset): Automatic weather station ID for this dataset.
        unit (str | Unset): Unit of rainfall amount.
        value (int | str | Unset): The publisher describes this as an integer total rainfall amount, but the example
            encodes values as strings, including "M" during maintenance. Both the documented integer and observed string
            representations are allowed.
    """

    automatic_weather_station: str | Unset = UNSET
    automatic_weather_station_id: str | Unset = UNSET
    unit: str | Unset = UNSET
    value: int | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automatic_weather_station = self.automatic_weather_station

        automatic_weather_station_id = self.automatic_weather_station_id

        unit = self.unit

        value: int | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if automatic_weather_station is not UNSET:
            field_dict["automaticWeatherStation"] = automatic_weather_station
        if automatic_weather_station_id is not UNSET:
            field_dict["automaticWeatherStationID"] = automatic_weather_station_id
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        automatic_weather_station = d.pop("automaticWeatherStation", UNSET)

        automatic_weather_station_id = d.pop("automaticWeatherStationID", UNSET)

        unit = d.pop("unit", UNSET)

        def _parse_value(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        hourly_rainfall_station = cls(
            automatic_weather_station=automatic_weather_station,
            automatic_weather_station_id=automatic_weather_station_id,
            unit=unit,
            value=value,
        )

        hourly_rainfall_station.additional_properties = d
        return hourly_rainfall_station

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
