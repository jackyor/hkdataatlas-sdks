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
        ele_yr (datetime.date | Unset):
        ele_tot_a (float | Unset):
        ele_dom_a (float | Unset):
        ele_com_a (float | Unset):
        ele_ind_a (float | Unset):
        ele_stlt_a (float | Unset):
        ele_exchi_a (float | Unset):
    """

    ele_yr: datetime.date | Unset = UNSET
    ele_tot_a: float | Unset = UNSET
    ele_dom_a: float | Unset = UNSET
    ele_com_a: float | Unset = UNSET
    ele_ind_a: float | Unset = UNSET
    ele_stlt_a: float | Unset = UNSET
    ele_exchi_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ele_yr: str | Unset = UNSET
        if not isinstance(self.ele_yr, Unset):
            ele_yr = self.ele_yr.isoformat()

        ele_tot_a = self.ele_tot_a

        ele_dom_a = self.ele_dom_a

        ele_com_a = self.ele_com_a

        ele_ind_a = self.ele_ind_a

        ele_stlt_a = self.ele_stlt_a

        ele_exchi_a = self.ele_exchi_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ele_yr is not UNSET:
            field_dict["Ele_yr"] = ele_yr
        if ele_tot_a is not UNSET:
            field_dict["Ele_tot_a"] = ele_tot_a
        if ele_dom_a is not UNSET:
            field_dict["Ele_dom_a"] = ele_dom_a
        if ele_com_a is not UNSET:
            field_dict["Ele_com_a"] = ele_com_a
        if ele_ind_a is not UNSET:
            field_dict["Ele_ind_a"] = ele_ind_a
        if ele_stlt_a is not UNSET:
            field_dict["Ele_stlt_a"] = ele_stlt_a
        if ele_exchi_a is not UNSET:
            field_dict["Ele_exchi_a"] = ele_exchi_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _ele_yr = d.pop("Ele_yr", UNSET)
        ele_yr: datetime.date | Unset
        if isinstance(_ele_yr, Unset):
            ele_yr = UNSET
        else:
            ele_yr = datetime.date.fromisoformat(_ele_yr)

        ele_tot_a = d.pop("Ele_tot_a", UNSET)

        ele_dom_a = d.pop("Ele_dom_a", UNSET)

        ele_com_a = d.pop("Ele_com_a", UNSET)

        ele_ind_a = d.pop("Ele_ind_a", UNSET)

        ele_stlt_a = d.pop("Ele_stlt_a", UNSET)

        ele_exchi_a = d.pop("Ele_exchi_a", UNSET)

        record = cls(
            ele_yr=ele_yr,
            ele_tot_a=ele_tot_a,
            ele_dom_a=ele_dom_a,
            ele_com_a=ele_com_a,
            ele_ind_a=ele_ind_a,
            ele_stlt_a=ele_stlt_a,
            ele_exchi_a=ele_exchi_a,
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
