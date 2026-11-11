from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObservedFlightNumber")


@_attrs_define
class ObservedFlightNumber:
    """Permissive structure of observed flight-number entries. The source describes a flight number, airline code, status
    code, and latest status, without establishing exact wire keys or types.

        Attributes:
            airline (Any | Unset): Observed key. The source describes an airline code.
            no (Any | Unset): Observed key. The source describes a flight number.
    """

    airline: Any | Unset = UNSET
    no: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        airline = self.airline

        no = self.no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if airline is not UNSET:
            field_dict["airline"] = airline
        if no is not UNSET:
            field_dict["no"] = no

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        airline = d.pop("airline", UNSET)

        no = d.pop("no", UNSET)

        observed_flight_number = cls(
            airline=airline,
            no=no,
        )

        observed_flight_number.additional_properties = d
        return observed_flight_number

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
