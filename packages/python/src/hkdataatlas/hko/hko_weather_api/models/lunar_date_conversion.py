from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LunarDateConversion")


@_attrs_define
class LunarDateConversion:
    """
    Attributes:
        lunar_date (str | Unset): Lunar date, in Traditional Chinese only. Example: 二月初十.
        lunar_year (str | Unset): Lunar year; Gan-Zhi and zodiac are in Traditional Chinese only. Example: 癸卯年，兔.
    """

    lunar_date: str | Unset = UNSET
    lunar_year: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lunar_date = self.lunar_date

        lunar_year = self.lunar_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lunar_date is not UNSET:
            field_dict["LunarDate"] = lunar_date
        if lunar_year is not UNSET:
            field_dict["LunarYear"] = lunar_year

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lunar_date = d.pop("LunarDate", UNSET)

        lunar_year = d.pop("LunarYear", UNSET)

        lunar_date_conversion = cls(
            lunar_date=lunar_date,
            lunar_year=lunar_year,
        )

        lunar_date_conversion.additional_properties = d
        return lunar_date_conversion

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
