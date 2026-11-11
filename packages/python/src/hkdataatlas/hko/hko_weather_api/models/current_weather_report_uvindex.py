from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentWeatherReportUvindex")


@_attrs_define
class CurrentWeatherReportUvindex:
    """
    Attributes:
        desc (str | Unset):
        message (str | Unset):
        place (str | Unset):
        record_desc (str | Unset):
        update_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
        value (float | str | Unset):
    """

    desc: str | Unset = UNSET
    message: str | Unset = UNSET
    place: str | Unset = UNSET
    record_desc: str | Unset = UNSET
    update_time: str | Unset = UNSET
    value: float | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desc = self.desc

        message = self.message

        place = self.place

        record_desc = self.record_desc

        update_time = self.update_time

        value: float | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desc is not UNSET:
            field_dict["desc"] = desc
        if message is not UNSET:
            field_dict["message"] = message
        if place is not UNSET:
            field_dict["place"] = place
        if record_desc is not UNSET:
            field_dict["recordDesc"] = record_desc
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        desc = d.pop("desc", UNSET)

        message = d.pop("message", UNSET)

        place = d.pop("place", UNSET)

        record_desc = d.pop("recordDesc", UNSET)

        update_time = d.pop("updateTime", UNSET)

        def _parse_value(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        current_weather_report_uvindex = cls(
            desc=desc,
            message=message,
            place=place,
            record_desc=record_desc,
            update_time=update_time,
            value=value,
        )

        current_weather_report_uvindex.additional_properties = d
        return current_weather_report_uvindex

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
