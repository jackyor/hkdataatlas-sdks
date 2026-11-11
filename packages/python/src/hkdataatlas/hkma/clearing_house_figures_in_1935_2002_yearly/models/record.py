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
        clh_yr (datetime.date | Unset):
        clh_tot_a (float | Unset):
        clh_yav_a (float | Unset):
    """

    clh_yr: datetime.date | Unset = UNSET
    clh_tot_a: float | Unset = UNSET
    clh_yav_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clh_yr: str | Unset = UNSET
        if not isinstance(self.clh_yr, Unset):
            clh_yr = self.clh_yr.isoformat()

        clh_tot_a = self.clh_tot_a

        clh_yav_a = self.clh_yav_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clh_yr is not UNSET:
            field_dict["Clh_yr"] = clh_yr
        if clh_tot_a is not UNSET:
            field_dict["Clh_tot_a"] = clh_tot_a
        if clh_yav_a is not UNSET:
            field_dict["Clh_yav_a"] = clh_yav_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _clh_yr = d.pop("Clh_yr", UNSET)
        clh_yr: datetime.date | Unset
        if isinstance(_clh_yr, Unset):
            clh_yr = UNSET
        else:
            clh_yr = datetime.date.fromisoformat(_clh_yr)

        clh_tot_a = d.pop("Clh_tot_a", UNSET)

        clh_yav_a = d.pop("Clh_yav_a", UNSET)

        record = cls(
            clh_yr=clh_yr,
            clh_tot_a=clh_tot_a,
            clh_yav_a=clh_yav_a,
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
