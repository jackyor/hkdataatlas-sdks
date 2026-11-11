from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eng_3d_address_eng_floor import Eng3DAddressEngFloor
    from ..models.eng_3d_address_eng_unit import Eng3DAddressEngUnit


T = TypeVar("T", bound="Eng3DAddress")


@_attrs_define
class Eng3DAddress:
    """Optional English floor and unit information; documented as available when `3d=1`.

    Attributes:
        eng_floor (Eng3DAddressEngFloor | Unset):
        eng_unit (Eng3DAddressEngUnit | Unset):
    """

    eng_floor: Eng3DAddressEngFloor | Unset = UNSET
    eng_unit: Eng3DAddressEngUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eng_floor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_floor, Unset):
            eng_floor = self.eng_floor.to_dict()

        eng_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_unit, Unset):
            eng_unit = self.eng_unit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eng_floor is not UNSET:
            field_dict["EngFloor"] = eng_floor
        if eng_unit is not UNSET:
            field_dict["EngUnit"] = eng_unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eng_3d_address_eng_floor import Eng3DAddressEngFloor
        from ..models.eng_3d_address_eng_unit import Eng3DAddressEngUnit

        d = dict(src_dict)
        _eng_floor = d.pop("EngFloor", UNSET)
        eng_floor: Eng3DAddressEngFloor | Unset
        if isinstance(_eng_floor, Unset):
            eng_floor = UNSET
        else:
            eng_floor = Eng3DAddressEngFloor.from_dict(_eng_floor)

        _eng_unit = d.pop("EngUnit", UNSET)
        eng_unit: Eng3DAddressEngUnit | Unset
        if isinstance(_eng_unit, Unset):
            eng_unit = UNSET
        else:
            eng_unit = Eng3DAddressEngUnit.from_dict(_eng_unit)

        eng_3d_address = cls(
            eng_floor=eng_floor,
            eng_unit=eng_unit,
        )

        eng_3d_address.additional_properties = d
        return eng_3d_address

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
