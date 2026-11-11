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
        tr_japimptl_a (float | Unset):
        tr_japexptl_a (float | Unset):
        tr_japimpchi_a (float | Unset):
        tr_japexpchi_a (float | Unset):
        tr_japimpmanc_a (float | Unset):
        tr_japexpmanc_a (float | Unset):
        tr_japimpkt_a (float | Unset):
        tr_japexpkt_a (float | Unset):
        tr_japimphk_a (float | Unset):
        tr_japexphk_a (float | Unset):
    """

    tr_yr: datetime.date | Unset = UNSET
    tr_japimptl_a: float | Unset = UNSET
    tr_japexptl_a: float | Unset = UNSET
    tr_japimpchi_a: float | Unset = UNSET
    tr_japexpchi_a: float | Unset = UNSET
    tr_japimpmanc_a: float | Unset = UNSET
    tr_japexpmanc_a: float | Unset = UNSET
    tr_japimpkt_a: float | Unset = UNSET
    tr_japexpkt_a: float | Unset = UNSET
    tr_japimphk_a: float | Unset = UNSET
    tr_japexphk_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tr_yr: str | Unset = UNSET
        if not isinstance(self.tr_yr, Unset):
            tr_yr = self.tr_yr.isoformat()

        tr_japimptl_a = self.tr_japimptl_a

        tr_japexptl_a = self.tr_japexptl_a

        tr_japimpchi_a = self.tr_japimpchi_a

        tr_japexpchi_a = self.tr_japexpchi_a

        tr_japimpmanc_a = self.tr_japimpmanc_a

        tr_japexpmanc_a = self.tr_japexpmanc_a

        tr_japimpkt_a = self.tr_japimpkt_a

        tr_japexpkt_a = self.tr_japexpkt_a

        tr_japimphk_a = self.tr_japimphk_a

        tr_japexphk_a = self.tr_japexphk_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tr_yr is not UNSET:
            field_dict["Tr_yr"] = tr_yr
        if tr_japimptl_a is not UNSET:
            field_dict["Tr_japimptl_a"] = tr_japimptl_a
        if tr_japexptl_a is not UNSET:
            field_dict["Tr_japexptl_a"] = tr_japexptl_a
        if tr_japimpchi_a is not UNSET:
            field_dict["Tr_japimpchi_a"] = tr_japimpchi_a
        if tr_japexpchi_a is not UNSET:
            field_dict["Tr_japexpchi_a"] = tr_japexpchi_a
        if tr_japimpmanc_a is not UNSET:
            field_dict["Tr_japimpmanc_a"] = tr_japimpmanc_a
        if tr_japexpmanc_a is not UNSET:
            field_dict["Tr_japexpmanc_a"] = tr_japexpmanc_a
        if tr_japimpkt_a is not UNSET:
            field_dict["Tr_japimpkt_a"] = tr_japimpkt_a
        if tr_japexpkt_a is not UNSET:
            field_dict["Tr_japexpkt_a"] = tr_japexpkt_a
        if tr_japimphk_a is not UNSET:
            field_dict["Tr_japimphk_a"] = tr_japimphk_a
        if tr_japexphk_a is not UNSET:
            field_dict["Tr_japexphk_a"] = tr_japexphk_a

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

        tr_japimptl_a = d.pop("Tr_japimptl_a", UNSET)

        tr_japexptl_a = d.pop("Tr_japexptl_a", UNSET)

        tr_japimpchi_a = d.pop("Tr_japimpchi_a", UNSET)

        tr_japexpchi_a = d.pop("Tr_japexpchi_a", UNSET)

        tr_japimpmanc_a = d.pop("Tr_japimpmanc_a", UNSET)

        tr_japexpmanc_a = d.pop("Tr_japexpmanc_a", UNSET)

        tr_japimpkt_a = d.pop("Tr_japimpkt_a", UNSET)

        tr_japexpkt_a = d.pop("Tr_japexpkt_a", UNSET)

        tr_japimphk_a = d.pop("Tr_japimphk_a", UNSET)

        tr_japexphk_a = d.pop("Tr_japexphk_a", UNSET)

        record = cls(
            tr_yr=tr_yr,
            tr_japimptl_a=tr_japimptl_a,
            tr_japexptl_a=tr_japexptl_a,
            tr_japimpchi_a=tr_japimpchi_a,
            tr_japexpchi_a=tr_japexpchi_a,
            tr_japimpmanc_a=tr_japimpmanc_a,
            tr_japexpmanc_a=tr_japexpmanc_a,
            tr_japimpkt_a=tr_japimpkt_a,
            tr_japexpkt_a=tr_japexpkt_a,
            tr_japimphk_a=tr_japimphk_a,
            tr_japexphk_a=tr_japexphk_a,
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
