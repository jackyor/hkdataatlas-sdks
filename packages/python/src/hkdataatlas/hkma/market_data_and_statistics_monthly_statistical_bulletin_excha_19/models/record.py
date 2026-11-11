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
        fixed_rate_1y_or_below (float | Unset):
        fixed_rate_1yto3y (float | Unset):
        fixed_rate_3yto5y (float | Unset):
        fixed_rate_5yto7y (float | Unset):
        fixed_rate_7y (float | Unset):
        fixed_rate_subtotal (float | Unset):
        floating_rate_1y_or_below (float | Unset):
        floating_rate_1yto3y (float | Unset):
        floating_rate_3yto5y (float | Unset):
        floating_rate_5yto7y (float | Unset):
        floating_rate_7y (float | Unset):
        floating_rate_subtotal (float | Unset):
        total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    fixed_rate_1y_or_below: float | Unset = UNSET
    fixed_rate_1yto3y: float | Unset = UNSET
    fixed_rate_3yto5y: float | Unset = UNSET
    fixed_rate_5yto7y: float | Unset = UNSET
    fixed_rate_7y: float | Unset = UNSET
    fixed_rate_subtotal: float | Unset = UNSET
    floating_rate_1y_or_below: float | Unset = UNSET
    floating_rate_1yto3y: float | Unset = UNSET
    floating_rate_3yto5y: float | Unset = UNSET
    floating_rate_5yto7y: float | Unset = UNSET
    floating_rate_7y: float | Unset = UNSET
    floating_rate_subtotal: float | Unset = UNSET
    total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        fixed_rate_1y_or_below = self.fixed_rate_1y_or_below

        fixed_rate_1yto3y = self.fixed_rate_1yto3y

        fixed_rate_3yto5y = self.fixed_rate_3yto5y

        fixed_rate_5yto7y = self.fixed_rate_5yto7y

        fixed_rate_7y = self.fixed_rate_7y

        fixed_rate_subtotal = self.fixed_rate_subtotal

        floating_rate_1y_or_below = self.floating_rate_1y_or_below

        floating_rate_1yto3y = self.floating_rate_1yto3y

        floating_rate_3yto5y = self.floating_rate_3yto5y

        floating_rate_5yto7y = self.floating_rate_5yto7y

        floating_rate_7y = self.floating_rate_7y

        floating_rate_subtotal = self.floating_rate_subtotal

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if fixed_rate_1y_or_below is not UNSET:
            field_dict["fixed_rate_1y_or_below"] = fixed_rate_1y_or_below
        if fixed_rate_1yto3y is not UNSET:
            field_dict["fixed_rate_1yto3y"] = fixed_rate_1yto3y
        if fixed_rate_3yto5y is not UNSET:
            field_dict["fixed_rate_3yto5y"] = fixed_rate_3yto5y
        if fixed_rate_5yto7y is not UNSET:
            field_dict["fixed_rate_5yto7y"] = fixed_rate_5yto7y
        if fixed_rate_7y is not UNSET:
            field_dict["fixed_rate_7y"] = fixed_rate_7y
        if fixed_rate_subtotal is not UNSET:
            field_dict["fixed_rate_subtotal"] = fixed_rate_subtotal
        if floating_rate_1y_or_below is not UNSET:
            field_dict["floating_rate_1y_or_below"] = floating_rate_1y_or_below
        if floating_rate_1yto3y is not UNSET:
            field_dict["floating_rate_1yto3y"] = floating_rate_1yto3y
        if floating_rate_3yto5y is not UNSET:
            field_dict["floating_rate_3yto5y"] = floating_rate_3yto5y
        if floating_rate_5yto7y is not UNSET:
            field_dict["floating_rate_5yto7y"] = floating_rate_5yto7y
        if floating_rate_7y is not UNSET:
            field_dict["floating_rate_7y"] = floating_rate_7y
        if floating_rate_subtotal is not UNSET:
            field_dict["floating_rate_subtotal"] = floating_rate_subtotal
        if total is not UNSET:
            field_dict["total"] = total

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

        fixed_rate_1y_or_below = d.pop("fixed_rate_1y_or_below", UNSET)

        fixed_rate_1yto3y = d.pop("fixed_rate_1yto3y", UNSET)

        fixed_rate_3yto5y = d.pop("fixed_rate_3yto5y", UNSET)

        fixed_rate_5yto7y = d.pop("fixed_rate_5yto7y", UNSET)

        fixed_rate_7y = d.pop("fixed_rate_7y", UNSET)

        fixed_rate_subtotal = d.pop("fixed_rate_subtotal", UNSET)

        floating_rate_1y_or_below = d.pop("floating_rate_1y_or_below", UNSET)

        floating_rate_1yto3y = d.pop("floating_rate_1yto3y", UNSET)

        floating_rate_3yto5y = d.pop("floating_rate_3yto5y", UNSET)

        floating_rate_5yto7y = d.pop("floating_rate_5yto7y", UNSET)

        floating_rate_7y = d.pop("floating_rate_7y", UNSET)

        floating_rate_subtotal = d.pop("floating_rate_subtotal", UNSET)

        total = d.pop("total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            fixed_rate_1y_or_below=fixed_rate_1y_or_below,
            fixed_rate_1yto3y=fixed_rate_1yto3y,
            fixed_rate_3yto5y=fixed_rate_3yto5y,
            fixed_rate_5yto7y=fixed_rate_5yto7y,
            fixed_rate_7y=fixed_rate_7y,
            fixed_rate_subtotal=fixed_rate_subtotal,
            floating_rate_1y_or_below=floating_rate_1y_or_below,
            floating_rate_1yto3y=floating_rate_1yto3y,
            floating_rate_3yto5y=floating_rate_3yto5y,
            floating_rate_5yto7y=floating_rate_5yto7y,
            floating_rate_7y=floating_rate_7y,
            floating_rate_subtotal=floating_rate_subtotal,
            total=total,
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
