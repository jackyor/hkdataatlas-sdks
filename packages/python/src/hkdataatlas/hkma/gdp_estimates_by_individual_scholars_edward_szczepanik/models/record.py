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
        gdp_yr (datetime.date | Unset):
        gdp_edszcurpr_a (float | Unset):
        gdp_edsz_47_pr_a (float | Unset):
        gdp_edszfc_a (float | Unset):
        gdp_edszcapfm_a (float | Unset):
    """

    gdp_yr: datetime.date | Unset = UNSET
    gdp_edszcurpr_a: float | Unset = UNSET
    gdp_edsz_47_pr_a: float | Unset = UNSET
    gdp_edszfc_a: float | Unset = UNSET
    gdp_edszcapfm_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gdp_yr: str | Unset = UNSET
        if not isinstance(self.gdp_yr, Unset):
            gdp_yr = self.gdp_yr.isoformat()

        gdp_edszcurpr_a = self.gdp_edszcurpr_a

        gdp_edsz_47_pr_a = self.gdp_edsz_47_pr_a

        gdp_edszfc_a = self.gdp_edszfc_a

        gdp_edszcapfm_a = self.gdp_edszcapfm_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gdp_yr is not UNSET:
            field_dict["Gdp_yr"] = gdp_yr
        if gdp_edszcurpr_a is not UNSET:
            field_dict["Gdp_edszcurpr_a"] = gdp_edszcurpr_a
        if gdp_edsz_47_pr_a is not UNSET:
            field_dict["Gdp_edsz47pr_a"] = gdp_edsz_47_pr_a
        if gdp_edszfc_a is not UNSET:
            field_dict["Gdp_edszfc_a"] = gdp_edszfc_a
        if gdp_edszcapfm_a is not UNSET:
            field_dict["Gdp_edszcapfm_a"] = gdp_edszcapfm_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _gdp_yr = d.pop("Gdp_yr", UNSET)
        gdp_yr: datetime.date | Unset
        if isinstance(_gdp_yr, Unset):
            gdp_yr = UNSET
        else:
            gdp_yr = datetime.date.fromisoformat(_gdp_yr)

        gdp_edszcurpr_a = d.pop("Gdp_edszcurpr_a", UNSET)

        gdp_edsz_47_pr_a = d.pop("Gdp_edsz47pr_a", UNSET)

        gdp_edszfc_a = d.pop("Gdp_edszfc_a", UNSET)

        gdp_edszcapfm_a = d.pop("Gdp_edszcapfm_a", UNSET)

        record = cls(
            gdp_yr=gdp_yr,
            gdp_edszcurpr_a=gdp_edszcurpr_a,
            gdp_edsz_47_pr_a=gdp_edsz_47_pr_a,
            gdp_edszfc_a=gdp_edszfc_a,
            gdp_edszcapfm_a=gdp_edszcapfm_a,
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
