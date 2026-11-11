from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Benchmark")


@_attrs_define
class Benchmark:
    """
    Attributes:
        end_of_month (datetime.date | Unset):
        ind_pricing_2y (float | Unset):
        ind_pricing_3y (float | Unset):
        ind_pricing_5y (float | Unset):
        ind_pricing_10y (float | Unset):
        ind_pricing_15y (float | Unset):
        closing_ref_rate_2y (float | Unset):
        closing_ref_rate_3y (float | Unset):
        closing_ref_rate_5y (float | Unset):
        closing_ref_rate_10y (float | Unset):
        closing_ref_rate_15y (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    ind_pricing_2y: float | Unset = UNSET
    ind_pricing_3y: float | Unset = UNSET
    ind_pricing_5y: float | Unset = UNSET
    ind_pricing_10y: float | Unset = UNSET
    ind_pricing_15y: float | Unset = UNSET
    closing_ref_rate_2y: float | Unset = UNSET
    closing_ref_rate_3y: float | Unset = UNSET
    closing_ref_rate_5y: float | Unset = UNSET
    closing_ref_rate_10y: float | Unset = UNSET
    closing_ref_rate_15y: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        ind_pricing_2y = self.ind_pricing_2y

        ind_pricing_3y = self.ind_pricing_3y

        ind_pricing_5y = self.ind_pricing_5y

        ind_pricing_10y = self.ind_pricing_10y

        ind_pricing_15y = self.ind_pricing_15y

        closing_ref_rate_2y = self.closing_ref_rate_2y

        closing_ref_rate_3y = self.closing_ref_rate_3y

        closing_ref_rate_5y = self.closing_ref_rate_5y

        closing_ref_rate_10y = self.closing_ref_rate_10y

        closing_ref_rate_15y = self.closing_ref_rate_15y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if ind_pricing_2y is not UNSET:
            field_dict["ind_pricing_2y"] = ind_pricing_2y
        if ind_pricing_3y is not UNSET:
            field_dict["ind_pricing_3y"] = ind_pricing_3y
        if ind_pricing_5y is not UNSET:
            field_dict["ind_pricing_5y"] = ind_pricing_5y
        if ind_pricing_10y is not UNSET:
            field_dict["ind_pricing_10y"] = ind_pricing_10y
        if ind_pricing_15y is not UNSET:
            field_dict["ind_pricing_15y"] = ind_pricing_15y
        if closing_ref_rate_2y is not UNSET:
            field_dict["closing_ref_rate_2y"] = closing_ref_rate_2y
        if closing_ref_rate_3y is not UNSET:
            field_dict["closing_ref_rate_3y"] = closing_ref_rate_3y
        if closing_ref_rate_5y is not UNSET:
            field_dict["closing_ref_rate_5y"] = closing_ref_rate_5y
        if closing_ref_rate_10y is not UNSET:
            field_dict["closing_ref_rate_10y"] = closing_ref_rate_10y
        if closing_ref_rate_15y is not UNSET:
            field_dict["closing_ref_rate_15y"] = closing_ref_rate_15y

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

        ind_pricing_2y = d.pop("ind_pricing_2y", UNSET)

        ind_pricing_3y = d.pop("ind_pricing_3y", UNSET)

        ind_pricing_5y = d.pop("ind_pricing_5y", UNSET)

        ind_pricing_10y = d.pop("ind_pricing_10y", UNSET)

        ind_pricing_15y = d.pop("ind_pricing_15y", UNSET)

        closing_ref_rate_2y = d.pop("closing_ref_rate_2y", UNSET)

        closing_ref_rate_3y = d.pop("closing_ref_rate_3y", UNSET)

        closing_ref_rate_5y = d.pop("closing_ref_rate_5y", UNSET)

        closing_ref_rate_10y = d.pop("closing_ref_rate_10y", UNSET)

        closing_ref_rate_15y = d.pop("closing_ref_rate_15y", UNSET)

        benchmark = cls(
            end_of_month=end_of_month,
            ind_pricing_2y=ind_pricing_2y,
            ind_pricing_3y=ind_pricing_3y,
            ind_pricing_5y=ind_pricing_5y,
            ind_pricing_10y=ind_pricing_10y,
            ind_pricing_15y=ind_pricing_15y,
            closing_ref_rate_2y=closing_ref_rate_2y,
            closing_ref_rate_3y=closing_ref_rate_3y,
            closing_ref_rate_5y=closing_ref_rate_5y,
            closing_ref_rate_10y=closing_ref_rate_10y,
            closing_ref_rate_15y=closing_ref_rate_15y,
        )

        benchmark.additional_properties = d
        return benchmark

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
