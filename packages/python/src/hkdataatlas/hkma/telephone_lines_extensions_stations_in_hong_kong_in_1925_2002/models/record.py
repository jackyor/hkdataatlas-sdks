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
        tel_yr (datetime.date | Unset):
        tel_exline_a (float | Unset):
        tel_extn_a (float | Unset):
        tel_totstn_a (float | Unset):
    """

    tel_yr: datetime.date | Unset = UNSET
    tel_exline_a: float | Unset = UNSET
    tel_extn_a: float | Unset = UNSET
    tel_totstn_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tel_yr: str | Unset = UNSET
        if not isinstance(self.tel_yr, Unset):
            tel_yr = self.tel_yr.isoformat()

        tel_exline_a = self.tel_exline_a

        tel_extn_a = self.tel_extn_a

        tel_totstn_a = self.tel_totstn_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tel_yr is not UNSET:
            field_dict["Tel_yr"] = tel_yr
        if tel_exline_a is not UNSET:
            field_dict["Tel_exline_a"] = tel_exline_a
        if tel_extn_a is not UNSET:
            field_dict["Tel_extn_a"] = tel_extn_a
        if tel_totstn_a is not UNSET:
            field_dict["Tel_totstn_a"] = tel_totstn_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _tel_yr = d.pop("Tel_yr", UNSET)
        tel_yr: datetime.date | Unset
        if isinstance(_tel_yr, Unset):
            tel_yr = UNSET
        else:
            tel_yr = datetime.date.fromisoformat(_tel_yr)

        tel_exline_a = d.pop("Tel_exline_a", UNSET)

        tel_extn_a = d.pop("Tel_extn_a", UNSET)

        tel_totstn_a = d.pop("Tel_totstn_a", UNSET)

        record = cls(
            tel_yr=tel_yr,
            tel_exline_a=tel_exline_a,
            tel_extn_a=tel_extn_a,
            tel_totstn_a=tel_totstn_a,
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
