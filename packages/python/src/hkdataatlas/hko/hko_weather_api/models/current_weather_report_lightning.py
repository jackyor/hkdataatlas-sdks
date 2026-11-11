from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentWeatherReportLightning")


@_attrs_define
class CurrentWeatherReportLightning:
    """
    Attributes:
        end_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
        occur (bool | Unset): Whether lightning occurred.
        place (str | Unset): Location.
        start_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
    """

    end_time: str | Unset = UNSET
    occur: bool | Unset = UNSET
    place: str | Unset = UNSET
    start_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time = self.end_time

        occur = self.occur

        place = self.place

        start_time = self.start_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if occur is not UNSET:
            field_dict["occur"] = occur
        if place is not UNSET:
            field_dict["place"] = place
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        end_time = d.pop("endTime", UNSET)

        occur = d.pop("occur", UNSET)

        place = d.pop("place", UNSET)

        start_time = d.pop("startTime", UNSET)

        current_weather_report_lightning = cls(
            end_time=end_time,
            occur=occur,
            place=place,
            start_time=start_time,
        )

        current_weather_report_lightning.additional_properties = d
        return current_weather_report_lightning

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
