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
        lbd_yr (datetime.date | Unset):
        lbd_tot_a (float | Unset):
        lbd_dtot_a (float | Unset):
        lbd_dhk_a (float | Unset):
        lbd_dfn_a (float | Unset):
        lbd_ttot_a (float | Unset):
        lbd_thk_a (float | Unset):
        lbd_tfn_a (float | Unset):
        lbd_stot_a (float | Unset):
        lbd_shk_a (float | Unset):
        lbd_sfn_a_number (float | Unset):
    """

    lbd_yr: datetime.date | Unset = UNSET
    lbd_tot_a: float | Unset = UNSET
    lbd_dtot_a: float | Unset = UNSET
    lbd_dhk_a: float | Unset = UNSET
    lbd_dfn_a: float | Unset = UNSET
    lbd_ttot_a: float | Unset = UNSET
    lbd_thk_a: float | Unset = UNSET
    lbd_tfn_a: float | Unset = UNSET
    lbd_stot_a: float | Unset = UNSET
    lbd_shk_a: float | Unset = UNSET
    lbd_sfn_a_number: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lbd_yr: str | Unset = UNSET
        if not isinstance(self.lbd_yr, Unset):
            lbd_yr = self.lbd_yr.isoformat()

        lbd_tot_a = self.lbd_tot_a

        lbd_dtot_a = self.lbd_dtot_a

        lbd_dhk_a = self.lbd_dhk_a

        lbd_dfn_a = self.lbd_dfn_a

        lbd_ttot_a = self.lbd_ttot_a

        lbd_thk_a = self.lbd_thk_a

        lbd_tfn_a = self.lbd_tfn_a

        lbd_stot_a = self.lbd_stot_a

        lbd_shk_a = self.lbd_shk_a

        lbd_sfn_a_number = self.lbd_sfn_a_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lbd_yr is not UNSET:
            field_dict["Lbd_yr"] = lbd_yr
        if lbd_tot_a is not UNSET:
            field_dict["Lbd_tot_a"] = lbd_tot_a
        if lbd_dtot_a is not UNSET:
            field_dict["Lbd_dtot_a"] = lbd_dtot_a
        if lbd_dhk_a is not UNSET:
            field_dict["Lbd_dhk_a"] = lbd_dhk_a
        if lbd_dfn_a is not UNSET:
            field_dict["Lbd_dfn_a"] = lbd_dfn_a
        if lbd_ttot_a is not UNSET:
            field_dict["Lbd_ttot_a"] = lbd_ttot_a
        if lbd_thk_a is not UNSET:
            field_dict["Lbd_thk_a"] = lbd_thk_a
        if lbd_tfn_a is not UNSET:
            field_dict["Lbd_tfn_a"] = lbd_tfn_a
        if lbd_stot_a is not UNSET:
            field_dict["Lbd_stot_a"] = lbd_stot_a
        if lbd_shk_a is not UNSET:
            field_dict["Lbd_shk_a"] = lbd_shk_a
        if lbd_sfn_a_number is not UNSET:
            field_dict["Lbd_sfn_a:Number"] = lbd_sfn_a_number

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _lbd_yr = d.pop("Lbd_yr", UNSET)
        lbd_yr: datetime.date | Unset
        if isinstance(_lbd_yr, Unset):
            lbd_yr = UNSET
        else:
            lbd_yr = datetime.date.fromisoformat(_lbd_yr)

        lbd_tot_a = d.pop("Lbd_tot_a", UNSET)

        lbd_dtot_a = d.pop("Lbd_dtot_a", UNSET)

        lbd_dhk_a = d.pop("Lbd_dhk_a", UNSET)

        lbd_dfn_a = d.pop("Lbd_dfn_a", UNSET)

        lbd_ttot_a = d.pop("Lbd_ttot_a", UNSET)

        lbd_thk_a = d.pop("Lbd_thk_a", UNSET)

        lbd_tfn_a = d.pop("Lbd_tfn_a", UNSET)

        lbd_stot_a = d.pop("Lbd_stot_a", UNSET)

        lbd_shk_a = d.pop("Lbd_shk_a", UNSET)

        lbd_sfn_a_number = d.pop("Lbd_sfn_a:Number", UNSET)

        record = cls(
            lbd_yr=lbd_yr,
            lbd_tot_a=lbd_tot_a,
            lbd_dtot_a=lbd_dtot_a,
            lbd_dhk_a=lbd_dhk_a,
            lbd_dfn_a=lbd_dfn_a,
            lbd_ttot_a=lbd_ttot_a,
            lbd_thk_a=lbd_thk_a,
            lbd_tfn_a=lbd_tfn_a,
            lbd_stot_a=lbd_stot_a,
            lbd_shk_a=lbd_shk_a,
            lbd_sfn_a_number=lbd_sfn_a_number,
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
