from __future__ import annotations

import datetime
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
        lb_yr (datetime.date | Unset):
        lb_brnum_a (float | Unset):
        lb_bran_a (float | Unset):
        lb_broff_a (float | Unset):
    """

    lb_yr: datetime.date | Unset = UNSET
    lb_brnum_a: float | Unset = UNSET
    lb_bran_a: float | Unset = UNSET
    lb_broff_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lb_yr: str | Unset = UNSET
        if not isinstance(self.lb_yr, Unset):
            lb_yr = self.lb_yr.isoformat()

        lb_brnum_a = self.lb_brnum_a

        lb_bran_a = self.lb_bran_a

        lb_broff_a = self.lb_broff_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lb_yr is not UNSET:
            field_dict["Lb_yr"] = lb_yr
        if lb_brnum_a is not UNSET:
            field_dict["Lb_brnum_a"] = lb_brnum_a
        if lb_bran_a is not UNSET:
            field_dict["Lb_bran_a"] = lb_bran_a
        if lb_broff_a is not UNSET:
            field_dict["Lb_broff_a"] = lb_broff_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _lb_yr = d.pop("Lb_yr", UNSET)
        lb_yr: datetime.date | Unset
        if isinstance(_lb_yr, Unset):
            lb_yr = UNSET
        else:
            lb_yr = datetime.date.fromisoformat(_lb_yr)

        lb_brnum_a = d.pop("Lb_brnum_a", UNSET)

        lb_bran_a = d.pop("Lb_bran_a", UNSET)

        lb_broff_a = d.pop("Lb_broff_a", UNSET)

        record = cls(
            lb_yr=lb_yr,
            lb_brnum_a=lb_brnum_a,
            lb_bran_a=lb_bran_a,
            lb_broff_a=lb_broff_a,
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
