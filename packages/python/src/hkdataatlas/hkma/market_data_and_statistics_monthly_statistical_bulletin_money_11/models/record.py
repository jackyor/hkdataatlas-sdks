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
        purchases_ncds_hkd (float | Unset):
        purchases_ncds_fc (float | Unset):
        purchases_ncds_total (float | Unset):
        sales_ncds_hkd (float | Unset):
        sales_ncds_fc (float | Unset):
        sales_ncds_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    purchases_ncds_hkd: float | Unset = UNSET
    purchases_ncds_fc: float | Unset = UNSET
    purchases_ncds_total: float | Unset = UNSET
    sales_ncds_hkd: float | Unset = UNSET
    sales_ncds_fc: float | Unset = UNSET
    sales_ncds_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        purchases_ncds_hkd = self.purchases_ncds_hkd

        purchases_ncds_fc = self.purchases_ncds_fc

        purchases_ncds_total = self.purchases_ncds_total

        sales_ncds_hkd = self.sales_ncds_hkd

        sales_ncds_fc = self.sales_ncds_fc

        sales_ncds_total = self.sales_ncds_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if purchases_ncds_hkd is not UNSET:
            field_dict["purchases_ncds_hkd"] = purchases_ncds_hkd
        if purchases_ncds_fc is not UNSET:
            field_dict["purchases_ncds_fc"] = purchases_ncds_fc
        if purchases_ncds_total is not UNSET:
            field_dict["purchases_ncds_total"] = purchases_ncds_total
        if sales_ncds_hkd is not UNSET:
            field_dict["sales_ncds_hkd"] = sales_ncds_hkd
        if sales_ncds_fc is not UNSET:
            field_dict["sales_ncds_fc"] = sales_ncds_fc
        if sales_ncds_total is not UNSET:
            field_dict["sales_ncds_total"] = sales_ncds_total

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

        purchases_ncds_hkd = d.pop("purchases_ncds_hkd", UNSET)

        purchases_ncds_fc = d.pop("purchases_ncds_fc", UNSET)

        purchases_ncds_total = d.pop("purchases_ncds_total", UNSET)

        sales_ncds_hkd = d.pop("sales_ncds_hkd", UNSET)

        sales_ncds_fc = d.pop("sales_ncds_fc", UNSET)

        sales_ncds_total = d.pop("sales_ncds_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            purchases_ncds_hkd=purchases_ncds_hkd,
            purchases_ncds_fc=purchases_ncds_fc,
            purchases_ncds_total=purchases_ncds_total,
            sales_ncds_hkd=sales_ncds_hkd,
            sales_ncds_fc=sales_ncds_fc,
            sales_ncds_total=sales_ncds_total,
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
