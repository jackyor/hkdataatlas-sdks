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
        institutional_2y (float | Unset):
        institutional_3y (float | Unset):
        institutional_5y (float | Unset):
        institutional_10y (float | Unset):
        institutional_15y (float | Unset):
        institutional_subtotal (float | Unset):
        retail_3y (float | Unset):
        retail_subtotal (float | Unset):
        total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    institutional_2y: float | Unset = UNSET
    institutional_3y: float | Unset = UNSET
    institutional_5y: float | Unset = UNSET
    institutional_10y: float | Unset = UNSET
    institutional_15y: float | Unset = UNSET
    institutional_subtotal: float | Unset = UNSET
    retail_3y: float | Unset = UNSET
    retail_subtotal: float | Unset = UNSET
    total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        institutional_2y = self.institutional_2y

        institutional_3y = self.institutional_3y

        institutional_5y = self.institutional_5y

        institutional_10y = self.institutional_10y

        institutional_15y = self.institutional_15y

        institutional_subtotal = self.institutional_subtotal

        retail_3y = self.retail_3y

        retail_subtotal = self.retail_subtotal

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if institutional_2y is not UNSET:
            field_dict["institutional_2y"] = institutional_2y
        if institutional_3y is not UNSET:
            field_dict["institutional_3y"] = institutional_3y
        if institutional_5y is not UNSET:
            field_dict["institutional_5y"] = institutional_5y
        if institutional_10y is not UNSET:
            field_dict["institutional_10y"] = institutional_10y
        if institutional_15y is not UNSET:
            field_dict["institutional_15y"] = institutional_15y
        if institutional_subtotal is not UNSET:
            field_dict["institutional_subtotal"] = institutional_subtotal
        if retail_3y is not UNSET:
            field_dict["retail_3y"] = retail_3y
        if retail_subtotal is not UNSET:
            field_dict["retail_subtotal"] = retail_subtotal
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

        institutional_2y = d.pop("institutional_2y", UNSET)

        institutional_3y = d.pop("institutional_3y", UNSET)

        institutional_5y = d.pop("institutional_5y", UNSET)

        institutional_10y = d.pop("institutional_10y", UNSET)

        institutional_15y = d.pop("institutional_15y", UNSET)

        institutional_subtotal = d.pop("institutional_subtotal", UNSET)

        retail_3y = d.pop("retail_3y", UNSET)

        retail_subtotal = d.pop("retail_subtotal", UNSET)

        total = d.pop("total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            institutional_2y=institutional_2y,
            institutional_3y=institutional_3y,
            institutional_5y=institutional_5y,
            institutional_10y=institutional_10y,
            institutional_15y=institutional_15y,
            institutional_subtotal=institutional_subtotal,
            retail_3y=retail_3y,
            retail_subtotal=retail_subtotal,
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
