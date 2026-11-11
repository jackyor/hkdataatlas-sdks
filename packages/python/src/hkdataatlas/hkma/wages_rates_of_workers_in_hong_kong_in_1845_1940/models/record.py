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
        wr_yr (datetime.date | Unset):
        wr_brlay_a (float | Unset):
        wr_carpe_a (float | Unset):
        wr_dserch_a (float | Unset):
        wr_dserfo_a (float | Unset):
        wr_join_a (float | Unset):
        wr_mason_a (float | Unset):
        wr_trchwn_a (float | Unset):
    """

    wr_yr: datetime.date | Unset = UNSET
    wr_brlay_a: float | Unset = UNSET
    wr_carpe_a: float | Unset = UNSET
    wr_dserch_a: float | Unset = UNSET
    wr_dserfo_a: float | Unset = UNSET
    wr_join_a: float | Unset = UNSET
    wr_mason_a: float | Unset = UNSET
    wr_trchwn_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wr_yr: str | Unset = UNSET
        if not isinstance(self.wr_yr, Unset):
            wr_yr = self.wr_yr.isoformat()

        wr_brlay_a = self.wr_brlay_a

        wr_carpe_a = self.wr_carpe_a

        wr_dserch_a = self.wr_dserch_a

        wr_dserfo_a = self.wr_dserfo_a

        wr_join_a = self.wr_join_a

        wr_mason_a = self.wr_mason_a

        wr_trchwn_a = self.wr_trchwn_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wr_yr is not UNSET:
            field_dict["Wr_yr"] = wr_yr
        if wr_brlay_a is not UNSET:
            field_dict["Wr_brlay_a"] = wr_brlay_a
        if wr_carpe_a is not UNSET:
            field_dict["Wr_carpe_a"] = wr_carpe_a
        if wr_dserch_a is not UNSET:
            field_dict["Wr_dserch_a"] = wr_dserch_a
        if wr_dserfo_a is not UNSET:
            field_dict["Wr_dserfo_a"] = wr_dserfo_a
        if wr_join_a is not UNSET:
            field_dict["Wr_join_a"] = wr_join_a
        if wr_mason_a is not UNSET:
            field_dict["Wr_mason_a"] = wr_mason_a
        if wr_trchwn_a is not UNSET:
            field_dict["Wr_trchwn_a"] = wr_trchwn_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _wr_yr = d.pop("Wr_yr", UNSET)
        wr_yr: datetime.date | Unset
        if isinstance(_wr_yr, Unset):
            wr_yr = UNSET
        else:
            wr_yr = datetime.date.fromisoformat(_wr_yr)

        wr_brlay_a = d.pop("Wr_brlay_a", UNSET)

        wr_carpe_a = d.pop("Wr_carpe_a", UNSET)

        wr_dserch_a = d.pop("Wr_dserch_a", UNSET)

        wr_dserfo_a = d.pop("Wr_dserfo_a", UNSET)

        wr_join_a = d.pop("Wr_join_a", UNSET)

        wr_mason_a = d.pop("Wr_mason_a", UNSET)

        wr_trchwn_a = d.pop("Wr_trchwn_a", UNSET)

        record = cls(
            wr_yr=wr_yr,
            wr_brlay_a=wr_brlay_a,
            wr_carpe_a=wr_carpe_a,
            wr_dserch_a=wr_dserch_a,
            wr_dserfo_a=wr_dserfo_a,
            wr_join_a=wr_join_a,
            wr_mason_a=wr_mason_a,
            wr_trchwn_a=wr_trchwn_a,
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
