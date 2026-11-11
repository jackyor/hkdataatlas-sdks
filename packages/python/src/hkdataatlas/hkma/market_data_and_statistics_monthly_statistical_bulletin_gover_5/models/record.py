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
        institutional_1y_or_below (float | Unset):
        institutional_1yto3y (float | Unset):
        institutional_3yto5y (float | Unset):
        institutional_5yto7y (float | Unset):
        institutional_over7y (float | Unset):
        institutional_subtotal (float | Unset):
        retail_1y_or_below (float | Unset):
        retail_1yto3y (float | Unset):
        retail_3yto5y (float | Unset):
        retail_5yto7y (float | Unset):
        retail_subtotal (float | Unset):
        total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    institutional_1y_or_below: float | Unset = UNSET
    institutional_1yto3y: float | Unset = UNSET
    institutional_3yto5y: float | Unset = UNSET
    institutional_5yto7y: float | Unset = UNSET
    institutional_over7y: float | Unset = UNSET
    institutional_subtotal: float | Unset = UNSET
    retail_1y_or_below: float | Unset = UNSET
    retail_1yto3y: float | Unset = UNSET
    retail_3yto5y: float | Unset = UNSET
    retail_5yto7y: float | Unset = UNSET
    retail_subtotal: float | Unset = UNSET
    total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        institutional_1y_or_below = self.institutional_1y_or_below

        institutional_1yto3y = self.institutional_1yto3y

        institutional_3yto5y = self.institutional_3yto5y

        institutional_5yto7y = self.institutional_5yto7y

        institutional_over7y = self.institutional_over7y

        institutional_subtotal = self.institutional_subtotal

        retail_1y_or_below = self.retail_1y_or_below

        retail_1yto3y = self.retail_1yto3y

        retail_3yto5y = self.retail_3yto5y

        retail_5yto7y = self.retail_5yto7y

        retail_subtotal = self.retail_subtotal

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if institutional_1y_or_below is not UNSET:
            field_dict["institutional_1y_or_below"] = institutional_1y_or_below
        if institutional_1yto3y is not UNSET:
            field_dict["institutional_1yto3y"] = institutional_1yto3y
        if institutional_3yto5y is not UNSET:
            field_dict["institutional_3yto5y"] = institutional_3yto5y
        if institutional_5yto7y is not UNSET:
            field_dict["institutional_5yto7y"] = institutional_5yto7y
        if institutional_over7y is not UNSET:
            field_dict["institutional_over7y"] = institutional_over7y
        if institutional_subtotal is not UNSET:
            field_dict["institutional_subtotal"] = institutional_subtotal
        if retail_1y_or_below is not UNSET:
            field_dict["retail_1y_or_below"] = retail_1y_or_below
        if retail_1yto3y is not UNSET:
            field_dict["retail_1yto3y"] = retail_1yto3y
        if retail_3yto5y is not UNSET:
            field_dict["retail_3yto5y"] = retail_3yto5y
        if retail_5yto7y is not UNSET:
            field_dict["retail_5yto7y"] = retail_5yto7y
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

        institutional_1y_or_below = d.pop("institutional_1y_or_below", UNSET)

        institutional_1yto3y = d.pop("institutional_1yto3y", UNSET)

        institutional_3yto5y = d.pop("institutional_3yto5y", UNSET)

        institutional_5yto7y = d.pop("institutional_5yto7y", UNSET)

        institutional_over7y = d.pop("institutional_over7y", UNSET)

        institutional_subtotal = d.pop("institutional_subtotal", UNSET)

        retail_1y_or_below = d.pop("retail_1y_or_below", UNSET)

        retail_1yto3y = d.pop("retail_1yto3y", UNSET)

        retail_3yto5y = d.pop("retail_3yto5y", UNSET)

        retail_5yto7y = d.pop("retail_5yto7y", UNSET)

        retail_subtotal = d.pop("retail_subtotal", UNSET)

        total = d.pop("total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            institutional_1y_or_below=institutional_1y_or_below,
            institutional_1yto3y=institutional_1yto3y,
            institutional_3yto5y=institutional_3yto5y,
            institutional_5yto7y=institutional_5yto7y,
            institutional_over7y=institutional_over7y,
            institutional_subtotal=institutional_subtotal,
            retail_1y_or_below=retail_1y_or_below,
            retail_1yto3y=retail_1yto3y,
            retail_3yto5y=retail_3yto5y,
            retail_5yto7y=retail_5yto7y,
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
