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
        institutional_1y (float | Unset):
        institutional_2y (float | Unset):
        institutional_3y (float | Unset):
        institutional_5y (float | Unset):
        institutional_7y (float | Unset):
        institutional_10y (float | Unset):
        institutional_20y (float | Unset):
        institutional_30y (float | Unset):
        total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    institutional_1y: float | Unset = UNSET
    institutional_2y: float | Unset = UNSET
    institutional_3y: float | Unset = UNSET
    institutional_5y: float | Unset = UNSET
    institutional_7y: float | Unset = UNSET
    institutional_10y: float | Unset = UNSET
    institutional_20y: float | Unset = UNSET
    institutional_30y: float | Unset = UNSET
    total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        institutional_1y = self.institutional_1y

        institutional_2y = self.institutional_2y

        institutional_3y = self.institutional_3y

        institutional_5y = self.institutional_5y

        institutional_7y = self.institutional_7y

        institutional_10y = self.institutional_10y

        institutional_20y = self.institutional_20y

        institutional_30y = self.institutional_30y

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if institutional_1y is not UNSET:
            field_dict["institutional_1y"] = institutional_1y
        if institutional_2y is not UNSET:
            field_dict["institutional_2y"] = institutional_2y
        if institutional_3y is not UNSET:
            field_dict["institutional_3y"] = institutional_3y
        if institutional_5y is not UNSET:
            field_dict["institutional_5y"] = institutional_5y
        if institutional_7y is not UNSET:
            field_dict["institutional_7y"] = institutional_7y
        if institutional_10y is not UNSET:
            field_dict["institutional_10y"] = institutional_10y
        if institutional_20y is not UNSET:
            field_dict["institutional_20y"] = institutional_20y
        if institutional_30y is not UNSET:
            field_dict["institutional_30y"] = institutional_30y
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

        institutional_1y = d.pop("institutional_1y", UNSET)

        institutional_2y = d.pop("institutional_2y", UNSET)

        institutional_3y = d.pop("institutional_3y", UNSET)

        institutional_5y = d.pop("institutional_5y", UNSET)

        institutional_7y = d.pop("institutional_7y", UNSET)

        institutional_10y = d.pop("institutional_10y", UNSET)

        institutional_20y = d.pop("institutional_20y", UNSET)

        institutional_30y = d.pop("institutional_30y", UNSET)

        total = d.pop("total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            institutional_1y=institutional_1y,
            institutional_2y=institutional_2y,
            institutional_3y=institutional_3y,
            institutional_5y=institutional_5y,
            institutional_7y=institutional_7y,
            institutional_10y=institutional_10y,
            institutional_20y=institutional_20y,
            institutional_30y=institutional_30y,
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
