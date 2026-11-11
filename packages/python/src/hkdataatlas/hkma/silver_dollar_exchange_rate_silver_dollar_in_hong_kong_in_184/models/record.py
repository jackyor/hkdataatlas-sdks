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
        exrt_yr (datetime.date | Unset):
        exrt_hksild_a (float | Unset):
        exrt_silhigh_a (float | Unset):
        exrt_sillow_a (float | Unset):
    """

    exrt_yr: datetime.date | Unset = UNSET
    exrt_hksild_a: float | Unset = UNSET
    exrt_silhigh_a: float | Unset = UNSET
    exrt_sillow_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exrt_yr: str | Unset = UNSET
        if not isinstance(self.exrt_yr, Unset):
            exrt_yr = self.exrt_yr.isoformat()

        exrt_hksild_a = self.exrt_hksild_a

        exrt_silhigh_a = self.exrt_silhigh_a

        exrt_sillow_a = self.exrt_sillow_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exrt_yr is not UNSET:
            field_dict["Exrt_yr"] = exrt_yr
        if exrt_hksild_a is not UNSET:
            field_dict["Exrt_hksild_a"] = exrt_hksild_a
        if exrt_silhigh_a is not UNSET:
            field_dict["Exrt_silhigh_a"] = exrt_silhigh_a
        if exrt_sillow_a is not UNSET:
            field_dict["Exrt_sillow_a"] = exrt_sillow_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _exrt_yr = d.pop("Exrt_yr", UNSET)
        exrt_yr: datetime.date | Unset
        if isinstance(_exrt_yr, Unset):
            exrt_yr = UNSET
        else:
            exrt_yr = datetime.date.fromisoformat(_exrt_yr)

        exrt_hksild_a = d.pop("Exrt_hksild_a", UNSET)

        exrt_silhigh_a = d.pop("Exrt_silhigh_a", UNSET)

        exrt_sillow_a = d.pop("Exrt_sillow_a", UNSET)

        record = cls(
            exrt_yr=exrt_yr,
            exrt_hksild_a=exrt_hksild_a,
            exrt_silhigh_a=exrt_silhigh_a,
            exrt_sillow_a=exrt_sillow_a,
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
