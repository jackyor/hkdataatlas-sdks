from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_weather_report_rainfall_place_item import (
        CurrentWeatherReportRainfallPlaceItem,
    )


T = TypeVar("T", bound="CurrentWeatherReportRainfall")


@_attrs_define
class CurrentWeatherReportRainfall:
    """
    Attributes:
        end_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
        place (list[CurrentWeatherReportRainfallPlaceItem] | Unset): Rainfall observation locations and records.
        start_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
        unit (str | Unset):
    """

    end_time: str | Unset = UNSET
    place: list[CurrentWeatherReportRainfallPlaceItem] | Unset = UNSET
    start_time: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time = self.end_time

        place: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.place, Unset):
            place = []
            for place_item_data in self.place:
                place_item = place_item_data.to_dict()
                place.append(place_item)

        start_time = self.start_time

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if place is not UNSET:
            field_dict["place"] = place
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.current_weather_report_rainfall_place_item import (
            CurrentWeatherReportRainfallPlaceItem,
        )

        d = dict(src_dict)
        end_time = d.pop("endTime", UNSET)

        _place = d.pop("place", UNSET)
        place: list[CurrentWeatherReportRainfallPlaceItem] | Unset = UNSET
        if _place is not UNSET:
            place = []
            for place_item_data in _place:
                place_item = CurrentWeatherReportRainfallPlaceItem.from_dict(
                    place_item_data
                )

                place.append(place_item)

        start_time = d.pop("startTime", UNSET)

        unit = d.pop("unit", UNSET)

        current_weather_report_rainfall = cls(
            end_time=end_time,
            place=place,
            start_time=start_time,
            unit=unit,
        )

        current_weather_report_rainfall.additional_properties = d
        return current_weather_report_rainfall

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
