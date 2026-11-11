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
        efb_1y_or_below (float | Unset):
        efn_1y_or_below (float | Unset):
        efn_1yto3y (float | Unset):
        efn_3yto5y (float | Unset):
        efn_5yto7y (float | Unset):
        efn_7yto10y (float | Unset):
        efn_10y (float | Unset):
        efn_subtotal (float | Unset):
        efbn_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    efb_1y_or_below: float | Unset = UNSET
    efn_1y_or_below: float | Unset = UNSET
    efn_1yto3y: float | Unset = UNSET
    efn_3yto5y: float | Unset = UNSET
    efn_5yto7y: float | Unset = UNSET
    efn_7yto10y: float | Unset = UNSET
    efn_10y: float | Unset = UNSET
    efn_subtotal: float | Unset = UNSET
    efbn_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        efb_1y_or_below = self.efb_1y_or_below

        efn_1y_or_below = self.efn_1y_or_below

        efn_1yto3y = self.efn_1yto3y

        efn_3yto5y = self.efn_3yto5y

        efn_5yto7y = self.efn_5yto7y

        efn_7yto10y = self.efn_7yto10y

        efn_10y = self.efn_10y

        efn_subtotal = self.efn_subtotal

        efbn_total = self.efbn_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if efb_1y_or_below is not UNSET:
            field_dict["efb_1y_or_below"] = efb_1y_or_below
        if efn_1y_or_below is not UNSET:
            field_dict["efn_1y_or_below"] = efn_1y_or_below
        if efn_1yto3y is not UNSET:
            field_dict["efn_1yto3y"] = efn_1yto3y
        if efn_3yto5y is not UNSET:
            field_dict["efn_3yto5y"] = efn_3yto5y
        if efn_5yto7y is not UNSET:
            field_dict["efn_5yto7y"] = efn_5yto7y
        if efn_7yto10y is not UNSET:
            field_dict["efn_7yto10y"] = efn_7yto10y
        if efn_10y is not UNSET:
            field_dict["efn_10y"] = efn_10y
        if efn_subtotal is not UNSET:
            field_dict["efn_subtotal"] = efn_subtotal
        if efbn_total is not UNSET:
            field_dict["efbn_total"] = efbn_total

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

        efb_1y_or_below = d.pop("efb_1y_or_below", UNSET)

        efn_1y_or_below = d.pop("efn_1y_or_below", UNSET)

        efn_1yto3y = d.pop("efn_1yto3y", UNSET)

        efn_3yto5y = d.pop("efn_3yto5y", UNSET)

        efn_5yto7y = d.pop("efn_5yto7y", UNSET)

        efn_7yto10y = d.pop("efn_7yto10y", UNSET)

        efn_10y = d.pop("efn_10y", UNSET)

        efn_subtotal = d.pop("efn_subtotal", UNSET)

        efbn_total = d.pop("efbn_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            efb_1y_or_below=efb_1y_or_below,
            efn_1y_or_below=efn_1y_or_below,
            efn_1yto3y=efn_1yto3y,
            efn_3yto5y=efn_3yto5y,
            efn_5yto7y=efn_5yto7y,
            efn_7yto10y=efn_7yto10y,
            efn_10y=efn_10y,
            efn_subtotal=efn_subtotal,
            efbn_total=efbn_total,
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
