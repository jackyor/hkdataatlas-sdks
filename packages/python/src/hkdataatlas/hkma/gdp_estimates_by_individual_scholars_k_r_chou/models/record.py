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
        gdp_choucurlow_a (float | Unset):
        gdp_choucurhi_a (float | Unset):
        gdp_choudep_a (float | Unset):
        gdp_chouotax_a (float | Unset):
        gdp_choudtax_a (float | Unset):
    """

    gdp_yr: datetime.date | Unset = UNSET
    gdp_choucurlow_a: float | Unset = UNSET
    gdp_choucurhi_a: float | Unset = UNSET
    gdp_choudep_a: float | Unset = UNSET
    gdp_chouotax_a: float | Unset = UNSET
    gdp_choudtax_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gdp_yr: str | Unset = UNSET
        if not isinstance(self.gdp_yr, Unset):
            gdp_yr = self.gdp_yr.isoformat()

        gdp_choucurlow_a = self.gdp_choucurlow_a

        gdp_choucurhi_a = self.gdp_choucurhi_a

        gdp_choudep_a = self.gdp_choudep_a

        gdp_chouotax_a = self.gdp_chouotax_a

        gdp_choudtax_a = self.gdp_choudtax_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gdp_yr is not UNSET:
            field_dict["Gdp_yr"] = gdp_yr
        if gdp_choucurlow_a is not UNSET:
            field_dict["Gdp_choucurlow_a"] = gdp_choucurlow_a
        if gdp_choucurhi_a is not UNSET:
            field_dict["Gdp_choucurhi_a"] = gdp_choucurhi_a
        if gdp_choudep_a is not UNSET:
            field_dict["Gdp_choudep_a"] = gdp_choudep_a
        if gdp_chouotax_a is not UNSET:
            field_dict["Gdp_chouotax_a"] = gdp_chouotax_a
        if gdp_choudtax_a is not UNSET:
            field_dict["Gdp_choudtax_a"] = gdp_choudtax_a

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

        gdp_choucurlow_a = d.pop("Gdp_choucurlow_a", UNSET)

        gdp_choucurhi_a = d.pop("Gdp_choucurhi_a", UNSET)

        gdp_choudep_a = d.pop("Gdp_choudep_a", UNSET)

        gdp_chouotax_a = d.pop("Gdp_chouotax_a", UNSET)

        gdp_choudtax_a = d.pop("Gdp_choudtax_a", UNSET)

        record = cls(
            gdp_yr=gdp_yr,
            gdp_choucurlow_a=gdp_choucurlow_a,
            gdp_choucurhi_a=gdp_choucurhi_a,
            gdp_choudep_a=gdp_choudep_a,
            gdp_chouotax_a=gdp_chouotax_a,
            gdp_choudtax_a=gdp_choudtax_a,
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
