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
        status_efb (str | Unset):
        status_efn (str | Unset):
        status_specified_instruments (str | Unset):
        status_gov_bond (str | Unset):
        is_retail_efn_distributor (str | Unset):
    """

    member_code: str | Unset = UNSET
    member_name: str | Unset = UNSET
    status_efb: str | Unset = UNSET
    status_efn: str | Unset = UNSET
    status_specified_instruments: str | Unset = UNSET
    status_gov_bond: str | Unset = UNSET
    is_retail_efn_distributor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_code = self.member_code

        member_name = self.member_name

        status_efb = self.status_efb

        status_efn = self.status_efn

        status_specified_instruments = self.status_specified_instruments

        status_gov_bond = self.status_gov_bond

        is_retail_efn_distributor = self.is_retail_efn_distributor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member_code is not UNSET:
            field_dict["member_code"] = member_code
        if member_name is not UNSET:
            field_dict["member_name"] = member_name
        if status_efb is not UNSET:
            field_dict["status_efb"] = status_efb
        if status_efn is not UNSET:
            field_dict["status_efn"] = status_efn
        if status_specified_instruments is not UNSET:
            field_dict["status_specified_instruments"] = status_specified_instruments
        if status_gov_bond is not UNSET:
            field_dict["status_gov_bond"] = status_gov_bond
        if is_retail_efn_distributor is not UNSET:
            field_dict["is_retail_efn_distributor"] = is_retail_efn_distributor

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        member_code = d.pop("member_code", UNSET)

        member_name = d.pop("member_name", UNSET)

        status_efb = d.pop("status_efb", UNSET)

        status_efn = d.pop("status_efn", UNSET)

        status_specified_instruments = d.pop("status_specified_instruments", UNSET)

        status_gov_bond = d.pop("status_gov_bond", UNSET)

        is_retail_efn_distributor = d.pop("is_retail_efn_distributor", UNSET)

        record = cls(
            member_code=member_code,
            member_name=member_name,
            status_efb=status_efb,
            status_efn=status_efn,
            status_specified_instruments=status_specified_instruments,
            status_gov_bond=status_gov_bond,
            is_retail_efn_distributor=is_retail_efn_distributor,
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
