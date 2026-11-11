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
        end_of_month (datetime.date | Unset):
        m1_hkd (float | Unset):
        m1_fc (float | Unset):
        m1_total (float | Unset):
        m2_hkd (float | Unset):
        m2_fc (float | Unset):
        m2_total (float | Unset):
        m3_hkd (float | Unset):
        m3_fc (float | Unset):
        m3_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    m1_hkd: float | Unset = UNSET
    m1_fc: float | Unset = UNSET
    m1_total: float | Unset = UNSET
    m2_hkd: float | Unset = UNSET
    m2_fc: float | Unset = UNSET
    m2_total: float | Unset = UNSET
    m3_hkd: float | Unset = UNSET
    m3_fc: float | Unset = UNSET
    m3_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        m1_hkd = self.m1_hkd

        m1_fc = self.m1_fc

        m1_total = self.m1_total

        m2_hkd = self.m2_hkd

        m2_fc = self.m2_fc

        m2_total = self.m2_total

        m3_hkd = self.m3_hkd

        m3_fc = self.m3_fc

        m3_total = self.m3_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if m1_hkd is not UNSET:
            field_dict["m1_hkd"] = m1_hkd
        if m1_fc is not UNSET:
            field_dict["m1_fc"] = m1_fc
        if m1_total is not UNSET:
            field_dict["m1_total"] = m1_total
        if m2_hkd is not UNSET:
            field_dict["m2_hkd"] = m2_hkd
        if m2_fc is not UNSET:
            field_dict["m2_fc"] = m2_fc
        if m2_total is not UNSET:
            field_dict["m2_total"] = m2_total
        if m3_hkd is not UNSET:
            field_dict["m3_hkd"] = m3_hkd
        if m3_fc is not UNSET:
            field_dict["m3_fc"] = m3_fc
        if m3_total is not UNSET:
            field_dict["m3_total"] = m3_total

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_month = d.pop("end_of_month", UNSET)
        end_of_month: datetime.date | Unset
        if isinstance(_end_of_month, Unset):
            end_of_month = UNSET
        else:
            end_of_month = datetime.date.fromisoformat(_end_of_month)

        m1_hkd = d.pop("m1_hkd", UNSET)

        m1_fc = d.pop("m1_fc", UNSET)

        m1_total = d.pop("m1_total", UNSET)

        m2_hkd = d.pop("m2_hkd", UNSET)

        m2_fc = d.pop("m2_fc", UNSET)

        m2_total = d.pop("m2_total", UNSET)

        m3_hkd = d.pop("m3_hkd", UNSET)

        m3_fc = d.pop("m3_fc", UNSET)

        m3_total = d.pop("m3_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            m1_hkd=m1_hkd,
            m1_fc=m1_fc,
            m1_total=m1_total,
            m2_hkd=m2_hkd,
            m2_fc=m2_fc,
            m2_total=m2_total,
            m3_hkd=m3_hkd,
            m3_fc=m3_fc,
            m3_total=m3_total,
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
