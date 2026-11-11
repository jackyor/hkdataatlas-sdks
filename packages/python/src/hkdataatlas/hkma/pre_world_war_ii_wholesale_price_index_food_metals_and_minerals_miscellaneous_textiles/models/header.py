from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Header")


@_attrs_define
class Header:
    """
    Attributes:
        err_code (str | Unset):
        err_msg (str | Unset):
        success (bool | Unset):
    """

    err_code: str | Unset = UNSET
    err_msg: str | Unset = UNSET
    success: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        err_code = self.err_code

        err_msg = self.err_msg

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if err_code is not UNSET:
            field_dict["err_code"] = err_code
        if err_msg is not UNSET:
            field_dict["err_msg"] = err_msg
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        err_code = d.pop("err_code", UNSET)

        err_msg = d.pop("err_msg", UNSET)

        success = d.pop("success", UNSET)

        header = cls(
            err_code=err_code,
            err_msg=err_msg,
            success=success,
        )

        header.additional_properties = d
        return header

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
