from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        name (str | Unset):
        local_address (str | Unset):
        principle_address (str | Unset):
        type_ (str | Unset):
        secstaff_reg_url (str | Unset):
    """

    name: str | Unset = UNSET
    local_address: str | Unset = UNSET
    principle_address: str | Unset = UNSET
    type_: str | Unset = UNSET
    secstaff_reg_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        local_address = self.local_address

        principle_address = self.principle_address

        type_ = self.type_

        secstaff_reg_url = self.secstaff_reg_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if local_address is not UNSET:
            field_dict["local_address"] = local_address
        if principle_address is not UNSET:
            field_dict["principle_address"] = principle_address
        if type_ is not UNSET:
            field_dict["type"] = type_
        if secstaff_reg_url is not UNSET:
            field_dict["secstaff_reg_url"] = secstaff_reg_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        local_address = d.pop("local_address", UNSET)

        principle_address = d.pop("principle_address", UNSET)

        type_ = d.pop("type", UNSET)

        secstaff_reg_url = d.pop("secstaff_reg_url", UNSET)

        record = cls(
            name=name,
            local_address=local_address,
            principle_address=principle_address,
            type_=type_,
            secstaff_reg_url=secstaff_reg_url,
        )

        record.additional_properties = d
        return record

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
