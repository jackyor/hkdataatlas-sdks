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
        efb_1y_or_below_val (float | Unset):
        efb_1y_or_below_vol (float | Unset):
        efn_1y_or_below_val (float | Unset):
        efn_1y_or_below_vol (float | Unset):
        efn_1yto3y_val (float | Unset):
        efn_1yto3y_vol (float | Unset):
        efn_3yto5y_val (float | Unset):
        efn_3yto5y_vol (float | Unset):
        efn_5yto7y_val (float | Unset):
        efn_5yto7y_vol (float | Unset):
        efn_7yto10y_val (float | Unset):
        efn_7yto10y_vol (float | Unset):
        efn_10y_val (float | Unset):
        efn_10y_vol (float | Unset):
        efn_subtotal_val (float | Unset):
        efn_subtotal_vol (float | Unset):
        efbn_total_val (float | Unset):
        efbn_total_vol (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    efb_1y_or_below_val: float | Unset = UNSET
    efb_1y_or_below_vol: float | Unset = UNSET
    efn_1y_or_below_val: float | Unset = UNSET
    efn_1y_or_below_vol: float | Unset = UNSET
    efn_1yto3y_val: float | Unset = UNSET
    efn_1yto3y_vol: float | Unset = UNSET
    efn_3yto5y_val: float | Unset = UNSET
    efn_3yto5y_vol: float | Unset = UNSET
    efn_5yto7y_val: float | Unset = UNSET
    efn_5yto7y_vol: float | Unset = UNSET
    efn_7yto10y_val: float | Unset = UNSET
    efn_7yto10y_vol: float | Unset = UNSET
    efn_10y_val: float | Unset = UNSET
    efn_10y_vol: float | Unset = UNSET
    efn_subtotal_val: float | Unset = UNSET
    efn_subtotal_vol: float | Unset = UNSET
    efbn_total_val: float | Unset = UNSET
    efbn_total_vol: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        efb_1y_or_below_val = self.efb_1y_or_below_val

        efb_1y_or_below_vol = self.efb_1y_or_below_vol

        efn_1y_or_below_val = self.efn_1y_or_below_val

        efn_1y_or_below_vol = self.efn_1y_or_below_vol

        efn_1yto3y_val = self.efn_1yto3y_val

        efn_1yto3y_vol = self.efn_1yto3y_vol

        efn_3yto5y_val = self.efn_3yto5y_val

        efn_3yto5y_vol = self.efn_3yto5y_vol

        efn_5yto7y_val = self.efn_5yto7y_val

        efn_5yto7y_vol = self.efn_5yto7y_vol

        efn_7yto10y_val = self.efn_7yto10y_val

        efn_7yto10y_vol = self.efn_7yto10y_vol

        efn_10y_val = self.efn_10y_val

        efn_10y_vol = self.efn_10y_vol

        efn_subtotal_val = self.efn_subtotal_val

        efn_subtotal_vol = self.efn_subtotal_vol

        efbn_total_val = self.efbn_total_val

        efbn_total_vol = self.efbn_total_vol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if efb_1y_or_below_val is not UNSET:
            field_dict["efb_1y_or_below_val"] = efb_1y_or_below_val
        if efb_1y_or_below_vol is not UNSET:
            field_dict["efb_1y_or_below_vol"] = efb_1y_or_below_vol
        if efn_1y_or_below_val is not UNSET:
            field_dict["efn_1y_or_below_val"] = efn_1y_or_below_val
        if efn_1y_or_below_vol is not UNSET:
            field_dict["efn_1y_or_below_vol"] = efn_1y_or_below_vol
        if efn_1yto3y_val is not UNSET:
            field_dict["efn_1yto3y_val"] = efn_1yto3y_val
        if efn_1yto3y_vol is not UNSET:
            field_dict["efn_1yto3y_vol"] = efn_1yto3y_vol
        if efn_3yto5y_val is not UNSET:
            field_dict["efn_3yto5y_val"] = efn_3yto5y_val
        if efn_3yto5y_vol is not UNSET:
            field_dict["efn_3yto5y_vol"] = efn_3yto5y_vol
        if efn_5yto7y_val is not UNSET:
            field_dict["efn_5yto7y_val"] = efn_5yto7y_val
        if efn_5yto7y_vol is not UNSET:
            field_dict["efn_5yto7y_vol"] = efn_5yto7y_vol
        if efn_7yto10y_val is not UNSET:
            field_dict["efn_7yto10y_val"] = efn_7yto10y_val
        if efn_7yto10y_vol is not UNSET:
            field_dict["efn_7yto10y_vol"] = efn_7yto10y_vol
        if efn_10y_val is not UNSET:
            field_dict["efn_10y_val"] = efn_10y_val
        if efn_10y_vol is not UNSET:
            field_dict["efn_10y_vol"] = efn_10y_vol
        if efn_subtotal_val is not UNSET:
            field_dict["efn_subtotal_val"] = efn_subtotal_val
        if efn_subtotal_vol is not UNSET:
            field_dict["efn_subtotal_vol"] = efn_subtotal_vol
        if efbn_total_val is not UNSET:
            field_dict["efbn_total_val"] = efbn_total_val
        if efbn_total_vol is not UNSET:
            field_dict["efbn_total_vol"] = efbn_total_vol

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

        efb_1y_or_below_val = d.pop("efb_1y_or_below_val", UNSET)

        efb_1y_or_below_vol = d.pop("efb_1y_or_below_vol", UNSET)

        efn_1y_or_below_val = d.pop("efn_1y_or_below_val", UNSET)

        efn_1y_or_below_vol = d.pop("efn_1y_or_below_vol", UNSET)

        efn_1yto3y_val = d.pop("efn_1yto3y_val", UNSET)

        efn_1yto3y_vol = d.pop("efn_1yto3y_vol", UNSET)

        efn_3yto5y_val = d.pop("efn_3yto5y_val", UNSET)

        efn_3yto5y_vol = d.pop("efn_3yto5y_vol", UNSET)

        efn_5yto7y_val = d.pop("efn_5yto7y_val", UNSET)

        efn_5yto7y_vol = d.pop("efn_5yto7y_vol", UNSET)

        efn_7yto10y_val = d.pop("efn_7yto10y_val", UNSET)

        efn_7yto10y_vol = d.pop("efn_7yto10y_vol", UNSET)

        efn_10y_val = d.pop("efn_10y_val", UNSET)

        efn_10y_vol = d.pop("efn_10y_vol", UNSET)

        efn_subtotal_val = d.pop("efn_subtotal_val", UNSET)

        efn_subtotal_vol = d.pop("efn_subtotal_vol", UNSET)

        efbn_total_val = d.pop("efbn_total_val", UNSET)

        efbn_total_vol = d.pop("efbn_total_vol", UNSET)

        record = cls(
            end_of_month=end_of_month,
            efb_1y_or_below_val=efb_1y_or_below_val,
            efb_1y_or_below_vol=efb_1y_or_below_vol,
            efn_1y_or_below_val=efn_1y_or_below_val,
            efn_1y_or_below_vol=efn_1y_or_below_vol,
            efn_1yto3y_val=efn_1yto3y_val,
            efn_1yto3y_vol=efn_1yto3y_vol,
            efn_3yto5y_val=efn_3yto5y_val,
            efn_3yto5y_vol=efn_3yto5y_vol,
            efn_5yto7y_val=efn_5yto7y_val,
            efn_5yto7y_vol=efn_5yto7y_vol,
            efn_7yto10y_val=efn_7yto10y_val,
            efn_7yto10y_vol=efn_7yto10y_vol,
            efn_10y_val=efn_10y_val,
            efn_10y_vol=efn_10y_vol,
            efn_subtotal_val=efn_subtotal_val,
            efn_subtotal_vol=efn_subtotal_vol,
            efbn_total_val=efbn_total_val,
            efbn_total_vol=efbn_total_vol,
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
