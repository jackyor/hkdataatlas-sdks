from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegistrationHistory")


@_attrs_define
class RegistrationHistory:
    """
    Attributes:
        reg_code (str | Unset):
        reg_inst_name (str | Unset):
        reg_act (str | Unset):
        effective_period (str | Unset):
        is_eo (str | Unset):
    """

    reg_code: str | Unset = UNSET
    reg_inst_name: str | Unset = UNSET
    reg_act: str | Unset = UNSET
    effective_period: str | Unset = UNSET
    is_eo: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reg_code = self.reg_code

        reg_inst_name = self.reg_inst_name

        reg_act = self.reg_act

        effective_period = self.effective_period

        is_eo = self.is_eo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reg_code is not UNSET:
            field_dict["reg_code"] = reg_code
        if reg_inst_name is not UNSET:
            field_dict["reg_inst_name"] = reg_inst_name
        if reg_act is not UNSET:
            field_dict["reg_act"] = reg_act
        if effective_period is not UNSET:
            field_dict["effective_period"] = effective_period
        if is_eo is not UNSET:
            field_dict["is_eo"] = is_eo

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reg_code = d.pop("reg_code", UNSET)

        reg_inst_name = d.pop("reg_inst_name", UNSET)

        reg_act = d.pop("reg_act", UNSET)

        effective_period = d.pop("effective_period", UNSET)

        is_eo = d.pop("is_eo", UNSET)

        registration_history = cls(
            reg_code=reg_code,
            reg_inst_name=reg_inst_name,
            reg_act=reg_act,
            effective_period=effective_period,
            is_eo=is_eo,
        )

        registration_history.additional_properties = d
        return registration_history

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
