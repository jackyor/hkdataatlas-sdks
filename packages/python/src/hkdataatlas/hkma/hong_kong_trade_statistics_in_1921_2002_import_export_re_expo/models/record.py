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
        tr_imp_a (float | Unset):
        tr_exp_a (float | Unset):
        tr_reexp_a (float | Unset):
        tr_trade_a (float | Unset):
    """

    tr_yr: datetime.date | Unset = UNSET
    tr_imp_a: float | Unset = UNSET
    tr_exp_a: float | Unset = UNSET
    tr_reexp_a: float | Unset = UNSET
    tr_trade_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tr_yr: str | Unset = UNSET
        if not isinstance(self.tr_yr, Unset):
            tr_yr = self.tr_yr.isoformat()

        tr_imp_a = self.tr_imp_a

        tr_exp_a = self.tr_exp_a

        tr_reexp_a = self.tr_reexp_a

        tr_trade_a = self.tr_trade_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tr_yr is not UNSET:
            field_dict["Tr_yr"] = tr_yr
        if tr_imp_a is not UNSET:
            field_dict["Tr_imp_a"] = tr_imp_a
        if tr_exp_a is not UNSET:
            field_dict["Tr_exp_a"] = tr_exp_a
        if tr_reexp_a is not UNSET:
            field_dict["Tr_reexp_a"] = tr_reexp_a
        if tr_trade_a is not UNSET:
            field_dict["Tr_trade_a"] = tr_trade_a

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

        tr_imp_a = d.pop("Tr_imp_a", UNSET)

        tr_exp_a = d.pop("Tr_exp_a", UNSET)

        tr_reexp_a = d.pop("Tr_reexp_a", UNSET)

        tr_trade_a = d.pop("Tr_trade_a", UNSET)

        record = cls(
            tr_yr=tr_yr,
            tr_imp_a=tr_imp_a,
            tr_exp_a=tr_exp_a,
            tr_reexp_a=tr_reexp_a,
            tr_trade_a=tr_trade_a,
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
