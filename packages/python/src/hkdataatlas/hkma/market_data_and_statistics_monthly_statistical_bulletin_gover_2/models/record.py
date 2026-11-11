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
        remain_1y_or_below_val (float | Unset):
        remain_1y_or_below_vol (float | Unset):
        remain_1yto3y_val (float | Unset):
        remain_1yto3y_vol (float | Unset):
        remain_3yto5y_val (float | Unset):
        remain_3yto5y_vol (float | Unset):
        remain_5yto7y_val (float | Unset):
        remain_5yto7y_vol (float | Unset):
        remain_7yto10y_val (float | Unset):
        remain_7yto10y_vol (float | Unset):
        remain_10yto15y_val (float | Unset):
        remain_10yto15y_vol (float | Unset):
        remain_total_val (float | Unset):
        remain_total_vol (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    remain_1y_or_below_val: float | Unset = UNSET
    remain_1y_or_below_vol: float | Unset = UNSET
    remain_1yto3y_val: float | Unset = UNSET
    remain_1yto3y_vol: float | Unset = UNSET
    remain_3yto5y_val: float | Unset = UNSET
    remain_3yto5y_vol: float | Unset = UNSET
    remain_5yto7y_val: float | Unset = UNSET
    remain_5yto7y_vol: float | Unset = UNSET
    remain_7yto10y_val: float | Unset = UNSET
    remain_7yto10y_vol: float | Unset = UNSET
    remain_10yto15y_val: float | Unset = UNSET
    remain_10yto15y_vol: float | Unset = UNSET
    remain_total_val: float | Unset = UNSET
    remain_total_vol: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        remain_1y_or_below_val = self.remain_1y_or_below_val

        remain_1y_or_below_vol = self.remain_1y_or_below_vol

        remain_1yto3y_val = self.remain_1yto3y_val

        remain_1yto3y_vol = self.remain_1yto3y_vol

        remain_3yto5y_val = self.remain_3yto5y_val

        remain_3yto5y_vol = self.remain_3yto5y_vol

        remain_5yto7y_val = self.remain_5yto7y_val

        remain_5yto7y_vol = self.remain_5yto7y_vol

        remain_7yto10y_val = self.remain_7yto10y_val

        remain_7yto10y_vol = self.remain_7yto10y_vol

        remain_10yto15y_val = self.remain_10yto15y_val

        remain_10yto15y_vol = self.remain_10yto15y_vol

        remain_total_val = self.remain_total_val

        remain_total_vol = self.remain_total_vol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if remain_1y_or_below_val is not UNSET:
            field_dict["remain_1y_or_below_val"] = remain_1y_or_below_val
        if remain_1y_or_below_vol is not UNSET:
            field_dict["remain_1y_or_below_vol"] = remain_1y_or_below_vol
        if remain_1yto3y_val is not UNSET:
            field_dict["remain_1yto3y_val"] = remain_1yto3y_val
        if remain_1yto3y_vol is not UNSET:
            field_dict["remain_1yto3y_vol"] = remain_1yto3y_vol
        if remain_3yto5y_val is not UNSET:
            field_dict["remain_3yto5y_val"] = remain_3yto5y_val
        if remain_3yto5y_vol is not UNSET:
            field_dict["remain_3yto5y_vol"] = remain_3yto5y_vol
        if remain_5yto7y_val is not UNSET:
            field_dict["remain_5yto7y_val"] = remain_5yto7y_val
        if remain_5yto7y_vol is not UNSET:
            field_dict["remain_5yto7y_vol"] = remain_5yto7y_vol
        if remain_7yto10y_val is not UNSET:
            field_dict["remain_7yto10y_val"] = remain_7yto10y_val
        if remain_7yto10y_vol is not UNSET:
            field_dict["remain_7yto10y_vol"] = remain_7yto10y_vol
        if remain_10yto15y_val is not UNSET:
            field_dict["remain_10yto15y_val"] = remain_10yto15y_val
        if remain_10yto15y_vol is not UNSET:
            field_dict["remain_10yto15y_vol"] = remain_10yto15y_vol
        if remain_total_val is not UNSET:
            field_dict["remain_total_val"] = remain_total_val
        if remain_total_vol is not UNSET:
            field_dict["remain_total_vol"] = remain_total_vol

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

        remain_1y_or_below_val = d.pop("remain_1y_or_below_val", UNSET)

        remain_1y_or_below_vol = d.pop("remain_1y_or_below_vol", UNSET)

        remain_1yto3y_val = d.pop("remain_1yto3y_val", UNSET)

        remain_1yto3y_vol = d.pop("remain_1yto3y_vol", UNSET)

        remain_3yto5y_val = d.pop("remain_3yto5y_val", UNSET)

        remain_3yto5y_vol = d.pop("remain_3yto5y_vol", UNSET)

        remain_5yto7y_val = d.pop("remain_5yto7y_val", UNSET)

        remain_5yto7y_vol = d.pop("remain_5yto7y_vol", UNSET)

        remain_7yto10y_val = d.pop("remain_7yto10y_val", UNSET)

        remain_7yto10y_vol = d.pop("remain_7yto10y_vol", UNSET)

        remain_10yto15y_val = d.pop("remain_10yto15y_val", UNSET)

        remain_10yto15y_vol = d.pop("remain_10yto15y_vol", UNSET)

        remain_total_val = d.pop("remain_total_val", UNSET)

        remain_total_vol = d.pop("remain_total_vol", UNSET)

        record = cls(
            end_of_month=end_of_month,
            remain_1y_or_below_val=remain_1y_or_below_val,
            remain_1y_or_below_vol=remain_1y_or_below_vol,
            remain_1yto3y_val=remain_1yto3y_val,
            remain_1yto3y_vol=remain_1yto3y_vol,
            remain_3yto5y_val=remain_3yto5y_val,
            remain_3yto5y_vol=remain_3yto5y_vol,
            remain_5yto7y_val=remain_5yto7y_val,
            remain_5yto7y_vol=remain_5yto7y_vol,
            remain_7yto10y_val=remain_7yto10y_val,
            remain_7yto10y_vol=remain_7yto10y_vol,
            remain_10yto15y_val=remain_10yto15y_val,
            remain_10yto15y_vol=remain_10yto15y_vol,
            remain_total_val=remain_total_val,
            remain_total_vol=remain_total_vol,
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
