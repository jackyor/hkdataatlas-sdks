from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Chi3DAddressChiUnit")


@_attrs_define
class Chi3DAddressChiUnit:
    """
    Attributes:
        unit_descriptor (str | Unset): Unit descriptor in Chinese, for example 室 or 舖.
        unit_no (str | Unset): Unit number, including non-numeric parts.
        unit_portion (str | Unset): Unit portion in Chinese.
    """

    unit_descriptor: str | Unset = UNSET
    unit_no: str | Unset = UNSET
    unit_portion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit_descriptor = self.unit_descriptor

        unit_no = self.unit_no

        unit_portion = self.unit_portion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_descriptor is not UNSET:
            field_dict["UnitDescriptor"] = unit_descriptor
        if unit_no is not UNSET:
            field_dict["UnitNo"] = unit_no
        if unit_portion is not UNSET:
            field_dict["UnitPortion"] = unit_portion

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        unit_descriptor = d.pop("UnitDescriptor", UNSET)

        unit_no = d.pop("UnitNo", UNSET)

        unit_portion = d.pop("UnitPortion", UNSET)

        chi_3d_address_chi_unit = cls(
            unit_descriptor=unit_descriptor,
            unit_no=unit_no,
            unit_portion=unit_portion,
        )

        chi_3d_address_chi_unit.additional_properties = d
        return chi_3d_address_chi_unit

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
