from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemperatureMeasurement")


@_attrs_define
class TemperatureMeasurement:
    """
    Attributes:
        depth (float | str | Unset): Depth value for soil temperature where supplied.
        place (str | Unset): Location.
        record_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
        unit (str | Unset): Unit.
        value (float | str | Unset): Measurement value; exact JSON wire type is not specified.
    """

    depth: float | str | Unset = UNSET
    place: str | Unset = UNSET
    record_time: str | Unset = UNSET
    unit: str | Unset = UNSET
    value: float | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        depth: float | str | Unset
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        place = self.place

        record_time = self.record_time

        unit = self.unit

        value: float | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if depth is not UNSET:
            field_dict["depth"] = depth
        if place is not UNSET:
            field_dict["place"] = place
        if record_time is not UNSET:
            field_dict["recordTime"] = record_time
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_depth(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        depth = _parse_depth(d.pop("depth", UNSET))

        place = d.pop("place", UNSET)

        record_time = d.pop("recordTime", UNSET)

        unit = d.pop("unit", UNSET)

        def _parse_value(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        temperature_measurement = cls(
            depth=depth,
            place=place,
            record_time=record_time,
            unit=unit,
            value=value,
        )

        temperature_measurement.additional_properties = d
        return temperature_measurement

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
