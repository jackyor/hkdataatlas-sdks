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
        member_code (str | Unset):
        member_name (str | Unset):
        bank_repo (str | Unset):
        cmubid (str | Unset):
        bond_connect (str | Unset):
    """

    member_code: str | Unset = UNSET
    member_name: str | Unset = UNSET
    bank_repo: str | Unset = UNSET
    cmubid: str | Unset = UNSET
    bond_connect: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_code = self.member_code

        member_name = self.member_name

        bank_repo = self.bank_repo

        cmubid = self.cmubid

        bond_connect = self.bond_connect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member_code is not UNSET:
            field_dict["member_code"] = member_code
        if member_name is not UNSET:
            field_dict["member_name"] = member_name
        if bank_repo is not UNSET:
            field_dict["bank_repo"] = bank_repo
        if cmubid is not UNSET:
            field_dict["cmubid"] = cmubid
        if bond_connect is not UNSET:
            field_dict["bond_connect"] = bond_connect

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        member_code = d.pop("member_code", UNSET)

        member_name = d.pop("member_name", UNSET)

        bank_repo = d.pop("bank_repo", UNSET)

        cmubid = d.pop("cmubid", UNSET)

        bond_connect = d.pop("bond_connect", UNSET)

        record = cls(
            member_code=member_code,
            member_name=member_name,
            bank_repo=bank_repo,
            cmubid=cmubid,
            bond_connect=bond_connect,
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
