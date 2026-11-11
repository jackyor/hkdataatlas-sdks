from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentRegistration")


@_attrs_define
class CurrentRegistration:
    """
    Attributes:
        reg_inst_name (str | Unset):
        reg_act (str | Unset):
        eng_first_date (str | Unset):
        is_eo (str | Unset):
        capacity (str | Unset):
        remarks (str | Unset):
    """

    reg_inst_name: str | Unset = UNSET
    reg_act: str | Unset = UNSET
    eng_first_date: str | Unset = UNSET
    is_eo: str | Unset = UNSET
    capacity: str | Unset = UNSET
    remarks: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reg_inst_name = self.reg_inst_name

        reg_act = self.reg_act

        eng_first_date = self.eng_first_date

        is_eo = self.is_eo

        capacity = self.capacity

        remarks = self.remarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reg_inst_name is not UNSET:
            field_dict["reg_inst_name"] = reg_inst_name
        if reg_act is not UNSET:
            field_dict["reg_act"] = reg_act
        if eng_first_date is not UNSET:
            field_dict["eng_first_date"] = eng_first_date
        if is_eo is not UNSET:
            field_dict["is_eo"] = is_eo
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reg_inst_name = d.pop("reg_inst_name", UNSET)

        reg_act = d.pop("reg_act", UNSET)

        eng_first_date = d.pop("eng_first_date", UNSET)

        is_eo = d.pop("is_eo", UNSET)

        capacity = d.pop("capacity", UNSET)

        remarks = d.pop("remarks", UNSET)

        current_registration = cls(
            reg_inst_name=reg_inst_name,
            reg_act=reg_act,
            eng_first_date=eng_first_date,
            is_eo=is_eo,
            capacity=capacity,
            remarks=remarks,
        )

        current_registration.additional_properties = d
        return current_registration

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
