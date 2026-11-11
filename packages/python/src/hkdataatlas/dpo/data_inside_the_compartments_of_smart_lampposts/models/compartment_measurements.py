from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompartmentMeasurements")


@_attrs_define
class CompartmentMeasurements:
    """Temperature and relative-humidity values for a compartment. The source documents string values; “////” indicates
    failure of quality control, and for compartments 3 and 4 “N.A.” indicates that the compartment does not exist.

        Attributes:
            rh (str | Unset): Relative humidity inside the compartment, in %, with resolution 0.1 %. “////” indicates
                failure of quality control; for compartments 3 and 4, “N.A.” indicates no such compartment.
            t0 (str | Unset): Temperature inside the compartment, in °C, with resolution 0.1 °C. “////” indicates failure of
                quality control; for compartments 3 and 4, “N.A.” indicates no such compartment.
    """

    rh: str | Unset = UNSET
    t0: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rh = self.rh

        t0 = self.t0

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rh is not UNSET:
            field_dict["RH"] = rh
        if t0 is not UNSET:
            field_dict["T0"] = t0

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rh = d.pop("RH", UNSET)

        t0 = d.pop("T0", UNSET)

        compartment_measurements = cls(
            rh=rh,
            t0=t0,
        )

        compartment_measurements.additional_properties = d
        return compartment_measurements

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
