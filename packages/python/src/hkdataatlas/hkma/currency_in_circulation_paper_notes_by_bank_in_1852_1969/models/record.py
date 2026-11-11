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
        cur_yr (datetime.date | Unset):
        cur_hsbc_a (float | Unset):
        cur_stchar_a (float | Unset):
        cur_merin_a (float | Unset):
        cur_orien_a (float | Unset):
        cur_nachina_a (float | Unset):
        cur_chara_a (float | Unset):
        cur_hkgov_a (float | Unset):
    """

    cur_yr: datetime.date | Unset = UNSET
    cur_hsbc_a: float | Unset = UNSET
    cur_stchar_a: float | Unset = UNSET
    cur_merin_a: float | Unset = UNSET
    cur_orien_a: float | Unset = UNSET
    cur_nachina_a: float | Unset = UNSET
    cur_chara_a: float | Unset = UNSET
    cur_hkgov_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cur_yr: str | Unset = UNSET
        if not isinstance(self.cur_yr, Unset):
            cur_yr = self.cur_yr.isoformat()

        cur_hsbc_a = self.cur_hsbc_a

        cur_stchar_a = self.cur_stchar_a

        cur_merin_a = self.cur_merin_a

        cur_orien_a = self.cur_orien_a

        cur_nachina_a = self.cur_nachina_a

        cur_chara_a = self.cur_chara_a

        cur_hkgov_a = self.cur_hkgov_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cur_yr is not UNSET:
            field_dict["Cur_yr"] = cur_yr
        if cur_hsbc_a is not UNSET:
            field_dict["Cur_hsbc_a"] = cur_hsbc_a
        if cur_stchar_a is not UNSET:
            field_dict["Cur_stchar_a"] = cur_stchar_a
        if cur_merin_a is not UNSET:
            field_dict["Cur_merin_a"] = cur_merin_a
        if cur_orien_a is not UNSET:
            field_dict["Cur_orien_a"] = cur_orien_a
        if cur_nachina_a is not UNSET:
            field_dict["Cur_nachina_a"] = cur_nachina_a
        if cur_chara_a is not UNSET:
            field_dict["Cur_chara_a"] = cur_chara_a
        if cur_hkgov_a is not UNSET:
            field_dict["Cur_hkgov_a"] = cur_hkgov_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _cur_yr = d.pop("Cur_yr", UNSET)
        cur_yr: datetime.date | Unset
        if isinstance(_cur_yr, Unset):
            cur_yr = UNSET
        else:
            cur_yr = datetime.date.fromisoformat(_cur_yr)

        cur_hsbc_a = d.pop("Cur_hsbc_a", UNSET)

        cur_stchar_a = d.pop("Cur_stchar_a", UNSET)

        cur_merin_a = d.pop("Cur_merin_a", UNSET)

        cur_orien_a = d.pop("Cur_orien_a", UNSET)

        cur_nachina_a = d.pop("Cur_nachina_a", UNSET)

        cur_chara_a = d.pop("Cur_chara_a", UNSET)

        cur_hkgov_a = d.pop("Cur_hkgov_a", UNSET)

        record = cls(
            cur_yr=cur_yr,
            cur_hsbc_a=cur_hsbc_a,
            cur_stchar_a=cur_stchar_a,
            cur_merin_a=cur_merin_a,
            cur_orien_a=cur_orien_a,
            cur_nachina_a=cur_nachina_a,
            cur_chara_a=cur_chara_a,
            cur_hkgov_a=cur_hkgov_a,
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
