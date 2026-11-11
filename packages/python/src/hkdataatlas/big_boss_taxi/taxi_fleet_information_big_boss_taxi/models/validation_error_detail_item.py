from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationErrorDetailItem")


@_attrs_define
class ValidationErrorDetailItem:
    """
    Attributes:
        loc (list[str] | Unset):  Example: ['body', 'lat'].
        msg (str | Unset):  Example: Field required.
        type_ (str | Unset):  Example: missing.
    """

    loc: list[str] | Unset = UNSET
    msg: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loc: list[str] | Unset = UNSET
        if not isinstance(self.loc, Unset):
            loc = self.loc

        msg = self.msg

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loc is not UNSET:
            field_dict["loc"] = loc
        if msg is not UNSET:
            field_dict["msg"] = msg
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        loc = cast(list[str], d.pop("loc", UNSET))

        msg = d.pop("msg", UNSET)

        type_ = d.pop("type", UNSET)

        validation_error_detail_item = cls(
            loc=loc,
            msg=msg,
            type_=type_,
        )

        validation_error_detail_item.additional_properties = d
        return validation_error_detail_item

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
