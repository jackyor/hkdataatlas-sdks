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
        tr_impukd_a (float | Unset):
        tr_impukp_a (float | Unset):
        tr_expukd_a (float | Unset):
        tr_expukp_a (float | Unset):
        tr_ukimptl_a (float | Unset):
        tr_ukexptl_a (float | Unset):
        tr_ukdomexp_a (float | Unset):
        tr_ukreexp_a (float | Unset):
    """

    tr_yr: datetime.date | Unset = UNSET
    tr_impukd_a: float | Unset = UNSET
    tr_impukp_a: float | Unset = UNSET
    tr_expukd_a: float | Unset = UNSET
    tr_expukp_a: float | Unset = UNSET
    tr_ukimptl_a: float | Unset = UNSET
    tr_ukexptl_a: float | Unset = UNSET
    tr_ukdomexp_a: float | Unset = UNSET
    tr_ukreexp_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tr_yr: str | Unset = UNSET
        if not isinstance(self.tr_yr, Unset):
            tr_yr = self.tr_yr.isoformat()

        tr_impukd_a = self.tr_impukd_a

        tr_impukp_a = self.tr_impukp_a

        tr_expukd_a = self.tr_expukd_a

        tr_expukp_a = self.tr_expukp_a

        tr_ukimptl_a = self.tr_ukimptl_a

        tr_ukexptl_a = self.tr_ukexptl_a

        tr_ukdomexp_a = self.tr_ukdomexp_a

        tr_ukreexp_a = self.tr_ukreexp_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tr_yr is not UNSET:
            field_dict["Tr_yr"] = tr_yr
        if tr_impukd_a is not UNSET:
            field_dict["Tr_impukd_a"] = tr_impukd_a
        if tr_impukp_a is not UNSET:
            field_dict["Tr_impukp_a"] = tr_impukp_a
        if tr_expukd_a is not UNSET:
            field_dict["Tr_expukd_a"] = tr_expukd_a
        if tr_expukp_a is not UNSET:
            field_dict["Tr_expukp_a"] = tr_expukp_a
        if tr_ukimptl_a is not UNSET:
            field_dict["Tr_ukimptl_a"] = tr_ukimptl_a
        if tr_ukexptl_a is not UNSET:
            field_dict["Tr_ukexptl_a"] = tr_ukexptl_a
        if tr_ukdomexp_a is not UNSET:
            field_dict["Tr_ukdomexp_a"] = tr_ukdomexp_a
        if tr_ukreexp_a is not UNSET:
            field_dict["Tr_ukreexp_a"] = tr_ukreexp_a

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

        tr_impukd_a = d.pop("Tr_impukd_a", UNSET)

        tr_impukp_a = d.pop("Tr_impukp_a", UNSET)

        tr_expukd_a = d.pop("Tr_expukd_a", UNSET)

        tr_expukp_a = d.pop("Tr_expukp_a", UNSET)

        tr_ukimptl_a = d.pop("Tr_ukimptl_a", UNSET)

        tr_ukexptl_a = d.pop("Tr_ukexptl_a", UNSET)

        tr_ukdomexp_a = d.pop("Tr_ukdomexp_a", UNSET)

        tr_ukreexp_a = d.pop("Tr_ukreexp_a", UNSET)

        record = cls(
            tr_yr=tr_yr,
            tr_impukd_a=tr_impukd_a,
            tr_impukp_a=tr_impukp_a,
            tr_expukd_a=tr_expukd_a,
            tr_expukp_a=tr_expukp_a,
            tr_ukimptl_a=tr_ukimptl_a,
            tr_ukexptl_a=tr_ukexptl_a,
            tr_ukdomexp_a=tr_ukdomexp_a,
            tr_ukreexp_a=tr_ukreexp_a,
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
