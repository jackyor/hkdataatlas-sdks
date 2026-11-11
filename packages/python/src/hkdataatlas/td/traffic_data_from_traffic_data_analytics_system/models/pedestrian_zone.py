from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PedestrianZone")


@_attrs_define
class PedestrianZone:
    """Pedestrian Zone feature information.

    Attributes:
        desc (str | Unset): Description.
        id (int | Unset): PED_ZONE_ID of the Pedestrian_Zone feature in IRN.
    """

    desc: str | Unset = UNSET
    id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desc = self.desc

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desc is not UNSET:
            field_dict["desc"] = desc
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        desc = d.pop("desc", UNSET)

        id = d.pop("id", UNSET)

        pedestrian_zone = cls(
            desc=desc,
            id=id,
        )

        pedestrian_zone.additional_properties = d
        return pedestrian_zone

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
