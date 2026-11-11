from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkstationGroup")


@_attrs_define
class WorkstationGroup:
    """A workstation group and its available workstation count.

    Attributes:
        available_wkt_number (float | str | Unset): The total number of available workstations in the group. The data
            dictionary declares the type as Numeric; the sample response represents it as an integer.
        group_id (str | Unset): The workstation group ID.
        group_name (str | Unset): The workstation group display name.
    """

    available_wkt_number: float | str | Unset = UNSET
    group_id: str | Unset = UNSET
    group_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_wkt_number: float | str | Unset
        if isinstance(self.available_wkt_number, Unset):
            available_wkt_number = UNSET
        else:
            available_wkt_number = self.available_wkt_number

        group_id = self.group_id

        group_name = self.group_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_wkt_number is not UNSET:
            field_dict["availableWktNumber"] = available_wkt_number
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if group_name is not UNSET:
            field_dict["groupName"] = group_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_available_wkt_number(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        available_wkt_number = _parse_available_wkt_number(
            d.pop("availableWktNumber", UNSET)
        )

        group_id = d.pop("groupId", UNSET)

        group_name = d.pop("groupName", UNSET)

        workstation_group = cls(
            available_wkt_number=available_wkt_number,
            group_id=group_id,
            group_name=group_name,
        )

        workstation_group.additional_properties = d
        return workstation_group

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
