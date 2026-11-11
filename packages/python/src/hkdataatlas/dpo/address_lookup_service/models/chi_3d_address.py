from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chi_3d_address_chi_floor import Chi3DAddressChiFloor
    from ..models.chi_3d_address_chi_unit import Chi3DAddressChiUnit


T = TypeVar("T", bound="Chi3DAddress")


@_attrs_define
class Chi3DAddress:
    """Optional Chinese floor and unit information; documented as available when `3d=1`.

    Attributes:
        chi_floor (Chi3DAddressChiFloor | Unset):
        chi_unit (Chi3DAddressChiUnit | Unset):
    """

    chi_floor: Chi3DAddressChiFloor | Unset = UNSET
    chi_unit: Chi3DAddressChiUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chi_floor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_floor, Unset):
            chi_floor = self.chi_floor.to_dict()

        chi_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_unit, Unset):
            chi_unit = self.chi_unit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chi_floor is not UNSET:
            field_dict["ChiFloor"] = chi_floor
        if chi_unit is not UNSET:
            field_dict["ChiUnit"] = chi_unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.chi_3d_address_chi_floor import Chi3DAddressChiFloor
        from ..models.chi_3d_address_chi_unit import Chi3DAddressChiUnit

        d = dict(src_dict)
        _chi_floor = d.pop("ChiFloor", UNSET)
        chi_floor: Chi3DAddressChiFloor | Unset
        if isinstance(_chi_floor, Unset):
            chi_floor = UNSET
        else:
            chi_floor = Chi3DAddressChiFloor.from_dict(_chi_floor)

        _chi_unit = d.pop("ChiUnit", UNSET)
        chi_unit: Chi3DAddressChiUnit | Unset
        if isinstance(_chi_unit, Unset):
            chi_unit = UNSET
        else:
            chi_unit = Chi3DAddressChiUnit.from_dict(_chi_unit)

        chi_3d_address = cls(
            chi_floor=chi_floor,
            chi_unit=chi_unit,
        )

        chi_3d_address.additional_properties = d
        return chi_3d_address

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
