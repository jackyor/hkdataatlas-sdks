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
        cur_paper_a (float | Unset):
        cur_coins_a (float | Unset):
        cur_tot_a (float | Unset):
    """

    cur_yr: datetime.date | Unset = UNSET
    cur_paper_a: float | Unset = UNSET
    cur_coins_a: float | Unset = UNSET
    cur_tot_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cur_yr: str | Unset = UNSET
        if not isinstance(self.cur_yr, Unset):
            cur_yr = self.cur_yr.isoformat()

        cur_paper_a = self.cur_paper_a

        cur_coins_a = self.cur_coins_a

        cur_tot_a = self.cur_tot_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cur_yr is not UNSET:
            field_dict["Cur_yr"] = cur_yr
        if cur_paper_a is not UNSET:
            field_dict["Cur_paper_a"] = cur_paper_a
        if cur_coins_a is not UNSET:
            field_dict["Cur_coins_a"] = cur_coins_a
        if cur_tot_a is not UNSET:
            field_dict["Cur_tot_a"] = cur_tot_a

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

        cur_paper_a = d.pop("Cur_paper_a", UNSET)

        cur_coins_a = d.pop("Cur_coins_a", UNSET)

        cur_tot_a = d.pop("Cur_tot_a", UNSET)

        record = cls(
            cur_yr=cur_yr,
            cur_paper_a=cur_paper_a,
            cur_coins_a=cur_coins_a,
            cur_tot_a=cur_tot_a,
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
