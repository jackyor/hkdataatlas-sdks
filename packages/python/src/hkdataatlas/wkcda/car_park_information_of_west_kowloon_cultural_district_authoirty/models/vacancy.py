from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vacancy")


@_attrs_define
class Vacancy:
    """
    Attributes:
        hourly (int | Unset): Hourly vacancy count in the published example.
        timestamp (str | Unset): Vacancy record timestamp; the example uses a date and time with fractional seconds.
        vehicle_type (str | Unset): Vehicle type code; the example uses P and other published records also use M.
    """

    hourly: int | Unset = UNSET
    timestamp: str | Unset = UNSET
    vehicle_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hourly = self.hourly

        timestamp = self.timestamp

        vehicle_type = self.vehicle_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hourly is not UNSET:
            field_dict["hourly"] = hourly
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if vehicle_type is not UNSET:
            field_dict["vehicleType"] = vehicle_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hourly = d.pop("hourly", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        vehicle_type = d.pop("vehicleType", UNSET)

        vacancy = cls(
            hourly=hourly,
            timestamp=timestamp,
            vehicle_type=vehicle_type,
        )

        vacancy.additional_properties = d
        return vacancy

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
