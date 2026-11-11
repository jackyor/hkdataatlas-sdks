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
        ad_turnover_1y (float | Unset):
        ad_turnover_2y (float | Unset):
        ad_turnover_3y (float | Unset):
        ad_turnover_5y (float | Unset):
        ad_turnover_7y (float | Unset):
        ad_turnover_10y (float | Unset):
        ad_turnover_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    ad_turnover_1y: float | Unset = UNSET
    ad_turnover_2y: float | Unset = UNSET
    ad_turnover_3y: float | Unset = UNSET
    ad_turnover_5y: float | Unset = UNSET
    ad_turnover_7y: float | Unset = UNSET
    ad_turnover_10y: float | Unset = UNSET
    ad_turnover_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        ad_turnover_1y = self.ad_turnover_1y

        ad_turnover_2y = self.ad_turnover_2y

        ad_turnover_3y = self.ad_turnover_3y

        ad_turnover_5y = self.ad_turnover_5y

        ad_turnover_7y = self.ad_turnover_7y

        ad_turnover_10y = self.ad_turnover_10y

        ad_turnover_total = self.ad_turnover_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if ad_turnover_1y is not UNSET:
            field_dict["ad_turnover_1y"] = ad_turnover_1y
        if ad_turnover_2y is not UNSET:
            field_dict["ad_turnover_2y"] = ad_turnover_2y
        if ad_turnover_3y is not UNSET:
            field_dict["ad_turnover_3y"] = ad_turnover_3y
        if ad_turnover_5y is not UNSET:
            field_dict["ad_turnover_5y"] = ad_turnover_5y
        if ad_turnover_7y is not UNSET:
            field_dict["ad_turnover_7y"] = ad_turnover_7y
        if ad_turnover_10y is not UNSET:
            field_dict["ad_turnover_10y"] = ad_turnover_10y
        if ad_turnover_total is not UNSET:
            field_dict["ad_turnover_total"] = ad_turnover_total

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

        ad_turnover_1y = d.pop("ad_turnover_1y", UNSET)

        ad_turnover_2y = d.pop("ad_turnover_2y", UNSET)

        ad_turnover_3y = d.pop("ad_turnover_3y", UNSET)

        ad_turnover_5y = d.pop("ad_turnover_5y", UNSET)

        ad_turnover_7y = d.pop("ad_turnover_7y", UNSET)

        ad_turnover_10y = d.pop("ad_turnover_10y", UNSET)

        ad_turnover_total = d.pop("ad_turnover_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            ad_turnover_1y=ad_turnover_1y,
            ad_turnover_2y=ad_turnover_2y,
            ad_turnover_3y=ad_turnover_3y,
            ad_turnover_5y=ad_turnover_5y,
            ad_turnover_7y=ad_turnover_7y,
            ad_turnover_10y=ad_turnover_10y,
            ad_turnover_total=ad_turnover_total,
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
