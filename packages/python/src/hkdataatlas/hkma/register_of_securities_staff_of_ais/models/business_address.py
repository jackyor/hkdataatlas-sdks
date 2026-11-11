from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessAddress")


@_attrs_define
class BusinessAddress:
    """
    Attributes:
        reg_inst_name (str | Unset):
        sfc_ce_num (str | Unset):
        business_address (str | Unset):
    """

    reg_inst_name: str | Unset = UNSET
    sfc_ce_num: str | Unset = UNSET
    business_address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reg_inst_name = self.reg_inst_name

        sfc_ce_num = self.sfc_ce_num

        business_address = self.business_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reg_inst_name is not UNSET:
            field_dict["reg_inst_name"] = reg_inst_name
        if sfc_ce_num is not UNSET:
            field_dict["sfc_ce_num"] = sfc_ce_num
        if business_address is not UNSET:
            field_dict["business_address"] = business_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reg_inst_name = d.pop("reg_inst_name", UNSET)

        sfc_ce_num = d.pop("sfc_ce_num", UNSET)

        business_address = d.pop("business_address", UNSET)

        business_address = cls(
            reg_inst_name=reg_inst_name,
            sfc_ce_num=sfc_ce_num,
            business_address=business_address,
        )

        business_address.additional_properties = d
        return business_address

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
