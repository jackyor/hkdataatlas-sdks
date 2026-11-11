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
        lbd_hsbc_year (datetime.date | Unset):
        lbd_hsbc_a (float | Unset):
    """

    lbd_hsbc_year: datetime.date | Unset = UNSET
    lbd_hsbc_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lbd_hsbc_year: str | Unset = UNSET
        if not isinstance(self.lbd_hsbc_year, Unset):
            lbd_hsbc_year = self.lbd_hsbc_year.isoformat()

        lbd_hsbc_a = self.lbd_hsbc_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lbd_hsbc_year is not UNSET:
            field_dict["Lbd_hsbc_year"] = lbd_hsbc_year
        if lbd_hsbc_a is not UNSET:
            field_dict["Lbd_hsbc_a"] = lbd_hsbc_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _lbd_hsbc_year = d.pop("Lbd_hsbc_year", UNSET)
        lbd_hsbc_year: datetime.date | Unset
        if isinstance(_lbd_hsbc_year, Unset):
            lbd_hsbc_year = UNSET
        else:
            lbd_hsbc_year = datetime.date.fromisoformat(_lbd_hsbc_year)

        lbd_hsbc_a = d.pop("Lbd_hsbc_a", UNSET)

        record = cls(
            lbd_hsbc_year=lbd_hsbc_year,
            lbd_hsbc_a=lbd_hsbc_a,
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
