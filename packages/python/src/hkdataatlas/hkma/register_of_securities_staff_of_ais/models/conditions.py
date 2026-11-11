from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Conditions")


@_attrs_define
class Conditions:
    """
    Attributes:
        reg_inst_name (str | Unset):
        effective_date (str | Unset):
        description (str | Unset):
    """

    reg_inst_name: str | Unset = UNSET
    effective_date: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reg_inst_name = self.reg_inst_name

        effective_date = self.effective_date

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reg_inst_name is not UNSET:
            field_dict["reg_inst_name"] = reg_inst_name
        if effective_date is not UNSET:
            field_dict["effective_date"] = effective_date
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reg_inst_name = d.pop("reg_inst_name", UNSET)

        effective_date = d.pop("effective_date", UNSET)

        description = d.pop("description", UNSET)

        conditions = cls(
            reg_inst_name=reg_inst_name,
            effective_date=effective_date,
            description=description,
        )

        conditions.additional_properties = d
        return conditions

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
