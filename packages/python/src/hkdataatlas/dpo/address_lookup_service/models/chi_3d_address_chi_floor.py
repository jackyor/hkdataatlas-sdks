from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Chi3DAddressChiFloor")


@_attrs_define
class Chi3DAddressChiFloor:
    """
    Attributes:
        floor_description (str | Unset): Floor description in Chinese, for example 大堂層, 地下上層, 天台 or 平台.
        floor_num (str | Unset): Floor number.
    """

    floor_description: str | Unset = UNSET
    floor_num: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        floor_description = self.floor_description

        floor_num = self.floor_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if floor_description is not UNSET:
            field_dict["FloorDescription"] = floor_description
        if floor_num is not UNSET:
            field_dict["FloorNum"] = floor_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        floor_description = d.pop("FloorDescription", UNSET)

        floor_num = d.pop("FloorNum", UNSET)

        chi_3d_address_chi_floor = cls(
            floor_description=floor_description,
            floor_num=floor_num,
        )

        chi_3d_address_chi_floor.additional_properties = d
        return chi_3d_address_chi_floor

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
