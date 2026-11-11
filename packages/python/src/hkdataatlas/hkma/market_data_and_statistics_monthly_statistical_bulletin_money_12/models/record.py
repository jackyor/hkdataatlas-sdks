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
        fixed_rate_less_than_3y (float | Unset):
        fixed_rate_3to5y (float | Unset):
        fixed_rate_more_than_5y (float | Unset):
        floating_rate_less_than_3y (float | Unset):
        floating_rate_3to5y (float | Unset):
        floating_rate_more_than_5y (float | Unset):
        osamt_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    fixed_rate_less_than_3y: float | Unset = UNSET
    fixed_rate_3to5y: float | Unset = UNSET
    fixed_rate_more_than_5y: float | Unset = UNSET
    floating_rate_less_than_3y: float | Unset = UNSET
    floating_rate_3to5y: float | Unset = UNSET
    floating_rate_more_than_5y: float | Unset = UNSET
    osamt_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        fixed_rate_less_than_3y = self.fixed_rate_less_than_3y

        fixed_rate_3to5y = self.fixed_rate_3to5y

        fixed_rate_more_than_5y = self.fixed_rate_more_than_5y

        floating_rate_less_than_3y = self.floating_rate_less_than_3y

        floating_rate_3to5y = self.floating_rate_3to5y

        floating_rate_more_than_5y = self.floating_rate_more_than_5y

        osamt_total = self.osamt_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if fixed_rate_less_than_3y is not UNSET:
            field_dict["fixed_rate_less_than_3y"] = fixed_rate_less_than_3y
        if fixed_rate_3to5y is not UNSET:
            field_dict["fixed_rate_3to5y"] = fixed_rate_3to5y
        if fixed_rate_more_than_5y is not UNSET:
            field_dict["fixed_rate_more_than_5y"] = fixed_rate_more_than_5y
        if floating_rate_less_than_3y is not UNSET:
            field_dict["floating_rate_less_than_3y"] = floating_rate_less_than_3y
        if floating_rate_3to5y is not UNSET:
            field_dict["floating_rate_3to5y"] = floating_rate_3to5y
        if floating_rate_more_than_5y is not UNSET:
            field_dict["floating_rate_more_than_5y"] = floating_rate_more_than_5y
        if osamt_total is not UNSET:
            field_dict["osamt_total"] = osamt_total

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

        fixed_rate_less_than_3y = d.pop("fixed_rate_less_than_3y", UNSET)

        fixed_rate_3to5y = d.pop("fixed_rate_3to5y", UNSET)

        fixed_rate_more_than_5y = d.pop("fixed_rate_more_than_5y", UNSET)

        floating_rate_less_than_3y = d.pop("floating_rate_less_than_3y", UNSET)

        floating_rate_3to5y = d.pop("floating_rate_3to5y", UNSET)

        floating_rate_more_than_5y = d.pop("floating_rate_more_than_5y", UNSET)

        osamt_total = d.pop("osamt_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            fixed_rate_less_than_3y=fixed_rate_less_than_3y,
            fixed_rate_3to5y=fixed_rate_3to5y,
            fixed_rate_more_than_5y=fixed_rate_more_than_5y,
            floating_rate_less_than_3y=floating_rate_less_than_3y,
            floating_rate_3to5y=floating_rate_3to5y,
            floating_rate_more_than_5y=floating_rate_more_than_5y,
            osamt_total=osamt_total,
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
