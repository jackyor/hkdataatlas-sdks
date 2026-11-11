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
        tr_yr (datetime.date | Unset):
        tr_chimphk_a (float | Unset):
        tr_chexphk_a (float | Unset):
        tr_chimptl_a (float | Unset):
        tr_chexptl_a (float | Unset):
        tr_chimphkper_a (float | Unset):
        tr_chexphkper_a (float | Unset):
    """

    tr_yr: datetime.date | Unset = UNSET
    tr_chimphk_a: float | Unset = UNSET
    tr_chexphk_a: float | Unset = UNSET
    tr_chimptl_a: float | Unset = UNSET
    tr_chexptl_a: float | Unset = UNSET
    tr_chimphkper_a: float | Unset = UNSET
    tr_chexphkper_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tr_yr: str | Unset = UNSET
        if not isinstance(self.tr_yr, Unset):
            tr_yr = self.tr_yr.isoformat()

        tr_chimphk_a = self.tr_chimphk_a

        tr_chexphk_a = self.tr_chexphk_a

        tr_chimptl_a = self.tr_chimptl_a

        tr_chexptl_a = self.tr_chexptl_a

        tr_chimphkper_a = self.tr_chimphkper_a

        tr_chexphkper_a = self.tr_chexphkper_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tr_yr is not UNSET:
            field_dict["Tr_yr"] = tr_yr
        if tr_chimphk_a is not UNSET:
            field_dict["Tr_chimphk_a"] = tr_chimphk_a
        if tr_chexphk_a is not UNSET:
            field_dict["Tr_chexphk_a"] = tr_chexphk_a
        if tr_chimptl_a is not UNSET:
            field_dict["Tr_chimptl_a"] = tr_chimptl_a
        if tr_chexptl_a is not UNSET:
            field_dict["Tr_chexptl_a"] = tr_chexptl_a
        if tr_chimphkper_a is not UNSET:
            field_dict["Tr_chimphkper_a"] = tr_chimphkper_a
        if tr_chexphkper_a is not UNSET:
            field_dict["Tr_chexphkper_a"] = tr_chexphkper_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _tr_yr = d.pop("Tr_yr", UNSET)
        tr_yr: datetime.date | Unset
        if isinstance(_tr_yr, Unset):
            tr_yr = UNSET
        else:
            tr_yr = datetime.date.fromisoformat(_tr_yr)

        tr_chimphk_a = d.pop("Tr_chimphk_a", UNSET)

        tr_chexphk_a = d.pop("Tr_chexphk_a", UNSET)

        tr_chimptl_a = d.pop("Tr_chimptl_a", UNSET)

        tr_chexptl_a = d.pop("Tr_chexptl_a", UNSET)

        tr_chimphkper_a = d.pop("Tr_chimphkper_a", UNSET)

        tr_chexphkper_a = d.pop("Tr_chexphkper_a", UNSET)

        record = cls(
            tr_yr=tr_yr,
            tr_chimphk_a=tr_chimphk_a,
            tr_chexphk_a=tr_chexphk_a,
            tr_chimptl_a=tr_chimptl_a,
            tr_chexptl_a=tr_chexptl_a,
            tr_chimphkper_a=tr_chimphkper_a,
            tr_chexphkper_a=tr_chexphkper_a,
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
