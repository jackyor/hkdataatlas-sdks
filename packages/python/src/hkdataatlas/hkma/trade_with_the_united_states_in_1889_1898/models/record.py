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
        tr_usimphkduty_a (float | Unset):
        tr_usimphkfree_a (float | Unset):
        tr_usimphktl_a (float | Unset):
        tr_usexphkduty_a (float | Unset):
        tr_usexphkfree_a (float | Unset):
        tr_usexphktl_a (float | Unset):
    """

    tr_yr: datetime.date | Unset = UNSET
    tr_usimphkduty_a: float | Unset = UNSET
    tr_usimphkfree_a: float | Unset = UNSET
    tr_usimphktl_a: float | Unset = UNSET
    tr_usexphkduty_a: float | Unset = UNSET
    tr_usexphkfree_a: float | Unset = UNSET
    tr_usexphktl_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tr_yr: str | Unset = UNSET
        if not isinstance(self.tr_yr, Unset):
            tr_yr = self.tr_yr.isoformat()

        tr_usimphkduty_a = self.tr_usimphkduty_a

        tr_usimphkfree_a = self.tr_usimphkfree_a

        tr_usimphktl_a = self.tr_usimphktl_a

        tr_usexphkduty_a = self.tr_usexphkduty_a

        tr_usexphkfree_a = self.tr_usexphkfree_a

        tr_usexphktl_a = self.tr_usexphktl_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tr_yr is not UNSET:
            field_dict["Tr_yr"] = tr_yr
        if tr_usimphkduty_a is not UNSET:
            field_dict["Tr_usimphkduty_a"] = tr_usimphkduty_a
        if tr_usimphkfree_a is not UNSET:
            field_dict["Tr_usimphkfree_a"] = tr_usimphkfree_a
        if tr_usimphktl_a is not UNSET:
            field_dict["Tr_usimphktl_a"] = tr_usimphktl_a
        if tr_usexphkduty_a is not UNSET:
            field_dict["Tr_usexphkduty_a"] = tr_usexphkduty_a
        if tr_usexphkfree_a is not UNSET:
            field_dict["Tr_usexphkfree_a"] = tr_usexphkfree_a
        if tr_usexphktl_a is not UNSET:
            field_dict["Tr_usexphktl_a"] = tr_usexphktl_a

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

        tr_usimphkduty_a = d.pop("Tr_usimphkduty_a", UNSET)

        tr_usimphkfree_a = d.pop("Tr_usimphkfree_a", UNSET)

        tr_usimphktl_a = d.pop("Tr_usimphktl_a", UNSET)

        tr_usexphkduty_a = d.pop("Tr_usexphkduty_a", UNSET)

        tr_usexphkfree_a = d.pop("Tr_usexphkfree_a", UNSET)

        tr_usexphktl_a = d.pop("Tr_usexphktl_a", UNSET)

        record = cls(
            tr_yr=tr_yr,
            tr_usimphkduty_a=tr_usimphkduty_a,
            tr_usimphkfree_a=tr_usimphkfree_a,
            tr_usimphktl_a=tr_usimphktl_a,
            tr_usexphkduty_a=tr_usexphkduty_a,
            tr_usexphkfree_a=tr_usexphkfree_a,
            tr_usexphktl_a=tr_usexphktl_a,
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
