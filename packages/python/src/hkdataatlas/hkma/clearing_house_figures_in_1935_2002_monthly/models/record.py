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
        clh_mth (datetime.date | Unset):
        clh_md_m (float | Unset):
    """

    clh_mth: datetime.date | Unset = UNSET
    clh_md_m: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clh_mth: str | Unset = UNSET
        if not isinstance(self.clh_mth, Unset):
            clh_mth = self.clh_mth.isoformat()

        clh_md_m = self.clh_md_m

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clh_mth is not UNSET:
            field_dict["Clh_mth"] = clh_mth
        if clh_md_m is not UNSET:
            field_dict["Clh_md_m"] = clh_md_m

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _clh_mth = d.pop("Clh_mth", UNSET)
        clh_mth: datetime.date | Unset
        if isinstance(_clh_mth, Unset):
            clh_mth = UNSET
        else:
            clh_mth = datetime.date.fromisoformat(_clh_mth)

        clh_md_m = d.pop("Clh_md_m", UNSET)

        record = cls(
            clh_mth=clh_mth,
            clh_md_m=clh_md_m,
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
