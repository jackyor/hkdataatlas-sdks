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
        fixed_rate_1y_or_below_val (float | Unset):
        fixed_rate_1y_or_below_vol (float | Unset):
        fixed_rate_1yto3y_val (float | Unset):
        fixed_rate_1yto3y_vol (float | Unset):
        fixed_rate_3yto5y_val (float | Unset):
        fixed_rate_3yto5y_vol (float | Unset):
        fixed_rate_5yto7y_val (float | Unset):
        fixed_rate_5yto7y_vol (float | Unset):
        fixed_rate_7y_val (float | Unset):
        fixed_rate_7y_vol (float | Unset):
        fixed_rate_subtotal_val (float | Unset):
        fixed_rate_subtotal_vol (float | Unset):
        floating_rate_1y_or_below_val (float | Unset):
        floating_rate_1y_or_below_vol (float | Unset):
        floating_rate_1yto3y_val (float | Unset):
        floating_rate_1yto3y_vol (float | Unset):
        floating_rate_3yto5y_val (float | Unset):
        floating_rate_3yto5y_vol (float | Unset):
        floating_rate_5yto7y_val (float | Unset):
        floating_rate_5yto7y_vol (float | Unset):
        floating_rate_7y_val (float | Unset):
        floating_rate_7y_vol (float | Unset):
        floating_rate_subtotal_val (float | Unset):
        floating_rate_subtotal_vol (float | Unset):
        total_val (float | Unset):
        total_vol (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    fixed_rate_1y_or_below_val: float | Unset = UNSET
    fixed_rate_1y_or_below_vol: float | Unset = UNSET
    fixed_rate_1yto3y_val: float | Unset = UNSET
    fixed_rate_1yto3y_vol: float | Unset = UNSET
    fixed_rate_3yto5y_val: float | Unset = UNSET
    fixed_rate_3yto5y_vol: float | Unset = UNSET
    fixed_rate_5yto7y_val: float | Unset = UNSET
    fixed_rate_5yto7y_vol: float | Unset = UNSET
    fixed_rate_7y_val: float | Unset = UNSET
    fixed_rate_7y_vol: float | Unset = UNSET
    fixed_rate_subtotal_val: float | Unset = UNSET
    fixed_rate_subtotal_vol: float | Unset = UNSET
    floating_rate_1y_or_below_val: float | Unset = UNSET
    floating_rate_1y_or_below_vol: float | Unset = UNSET
    floating_rate_1yto3y_val: float | Unset = UNSET
    floating_rate_1yto3y_vol: float | Unset = UNSET
    floating_rate_3yto5y_val: float | Unset = UNSET
    floating_rate_3yto5y_vol: float | Unset = UNSET
    floating_rate_5yto7y_val: float | Unset = UNSET
    floating_rate_5yto7y_vol: float | Unset = UNSET
    floating_rate_7y_val: float | Unset = UNSET
    floating_rate_7y_vol: float | Unset = UNSET
    floating_rate_subtotal_val: float | Unset = UNSET
    floating_rate_subtotal_vol: float | Unset = UNSET
    total_val: float | Unset = UNSET
    total_vol: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        fixed_rate_1y_or_below_val = self.fixed_rate_1y_or_below_val

        fixed_rate_1y_or_below_vol = self.fixed_rate_1y_or_below_vol

        fixed_rate_1yto3y_val = self.fixed_rate_1yto3y_val

        fixed_rate_1yto3y_vol = self.fixed_rate_1yto3y_vol

        fixed_rate_3yto5y_val = self.fixed_rate_3yto5y_val

        fixed_rate_3yto5y_vol = self.fixed_rate_3yto5y_vol

        fixed_rate_5yto7y_val = self.fixed_rate_5yto7y_val

        fixed_rate_5yto7y_vol = self.fixed_rate_5yto7y_vol

        fixed_rate_7y_val = self.fixed_rate_7y_val

        fixed_rate_7y_vol = self.fixed_rate_7y_vol

        fixed_rate_subtotal_val = self.fixed_rate_subtotal_val

        fixed_rate_subtotal_vol = self.fixed_rate_subtotal_vol

        floating_rate_1y_or_below_val = self.floating_rate_1y_or_below_val

        floating_rate_1y_or_below_vol = self.floating_rate_1y_or_below_vol

        floating_rate_1yto3y_val = self.floating_rate_1yto3y_val

        floating_rate_1yto3y_vol = self.floating_rate_1yto3y_vol

        floating_rate_3yto5y_val = self.floating_rate_3yto5y_val

        floating_rate_3yto5y_vol = self.floating_rate_3yto5y_vol

        floating_rate_5yto7y_val = self.floating_rate_5yto7y_val

        floating_rate_5yto7y_vol = self.floating_rate_5yto7y_vol

        floating_rate_7y_val = self.floating_rate_7y_val

        floating_rate_7y_vol = self.floating_rate_7y_vol

        floating_rate_subtotal_val = self.floating_rate_subtotal_val

        floating_rate_subtotal_vol = self.floating_rate_subtotal_vol

        total_val = self.total_val

        total_vol = self.total_vol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if fixed_rate_1y_or_below_val is not UNSET:
            field_dict["fixed_rate_1y_or_below_val"] = fixed_rate_1y_or_below_val
        if fixed_rate_1y_or_below_vol is not UNSET:
            field_dict["fixed_rate_1y_or_below_vol"] = fixed_rate_1y_or_below_vol
        if fixed_rate_1yto3y_val is not UNSET:
            field_dict["fixed_rate_1yto3y_val"] = fixed_rate_1yto3y_val
        if fixed_rate_1yto3y_vol is not UNSET:
            field_dict["fixed_rate_1yto3y_vol"] = fixed_rate_1yto3y_vol
        if fixed_rate_3yto5y_val is not UNSET:
            field_dict["fixed_rate_3yto5y_val"] = fixed_rate_3yto5y_val
        if fixed_rate_3yto5y_vol is not UNSET:
            field_dict["fixed_rate_3yto5y_vol"] = fixed_rate_3yto5y_vol
        if fixed_rate_5yto7y_val is not UNSET:
            field_dict["fixed_rate_5yto7y_val"] = fixed_rate_5yto7y_val
        if fixed_rate_5yto7y_vol is not UNSET:
            field_dict["fixed_rate_5yto7y_vol"] = fixed_rate_5yto7y_vol
        if fixed_rate_7y_val is not UNSET:
            field_dict["fixed_rate_7y_val"] = fixed_rate_7y_val
        if fixed_rate_7y_vol is not UNSET:
            field_dict["fixed_rate_7y_vol"] = fixed_rate_7y_vol
        if fixed_rate_subtotal_val is not UNSET:
            field_dict["fixed_rate_subtotal_val"] = fixed_rate_subtotal_val
        if fixed_rate_subtotal_vol is not UNSET:
            field_dict["fixed_rate_subtotal_vol"] = fixed_rate_subtotal_vol
        if floating_rate_1y_or_below_val is not UNSET:
            field_dict["floating_rate_1y_or_below_val"] = floating_rate_1y_or_below_val
        if floating_rate_1y_or_below_vol is not UNSET:
            field_dict["floating_rate_1y_or_below_vol"] = floating_rate_1y_or_below_vol
        if floating_rate_1yto3y_val is not UNSET:
            field_dict["floating_rate_1yto3y_val"] = floating_rate_1yto3y_val
        if floating_rate_1yto3y_vol is not UNSET:
            field_dict["floating_rate_1yto3y_vol"] = floating_rate_1yto3y_vol
        if floating_rate_3yto5y_val is not UNSET:
            field_dict["floating_rate_3yto5y_val"] = floating_rate_3yto5y_val
        if floating_rate_3yto5y_vol is not UNSET:
            field_dict["floating_rate_3yto5y_vol"] = floating_rate_3yto5y_vol
        if floating_rate_5yto7y_val is not UNSET:
            field_dict["floating_rate_5yto7y_val"] = floating_rate_5yto7y_val
        if floating_rate_5yto7y_vol is not UNSET:
            field_dict["floating_rate_5yto7y_vol"] = floating_rate_5yto7y_vol
        if floating_rate_7y_val is not UNSET:
            field_dict["floating_rate_7y_val"] = floating_rate_7y_val
        if floating_rate_7y_vol is not UNSET:
            field_dict["floating_rate_7y_vol"] = floating_rate_7y_vol
        if floating_rate_subtotal_val is not UNSET:
            field_dict["floating_rate_subtotal_val"] = floating_rate_subtotal_val
        if floating_rate_subtotal_vol is not UNSET:
            field_dict["floating_rate_subtotal_vol"] = floating_rate_subtotal_vol
        if total_val is not UNSET:
            field_dict["total_val"] = total_val
        if total_vol is not UNSET:
            field_dict["total_vol"] = total_vol

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

        fixed_rate_1y_or_below_val = d.pop("fixed_rate_1y_or_below_val", UNSET)

        fixed_rate_1y_or_below_vol = d.pop("fixed_rate_1y_or_below_vol", UNSET)

        fixed_rate_1yto3y_val = d.pop("fixed_rate_1yto3y_val", UNSET)

        fixed_rate_1yto3y_vol = d.pop("fixed_rate_1yto3y_vol", UNSET)

        fixed_rate_3yto5y_val = d.pop("fixed_rate_3yto5y_val", UNSET)

        fixed_rate_3yto5y_vol = d.pop("fixed_rate_3yto5y_vol", UNSET)

        fixed_rate_5yto7y_val = d.pop("fixed_rate_5yto7y_val", UNSET)

        fixed_rate_5yto7y_vol = d.pop("fixed_rate_5yto7y_vol", UNSET)

        fixed_rate_7y_val = d.pop("fixed_rate_7y_val", UNSET)

        fixed_rate_7y_vol = d.pop("fixed_rate_7y_vol", UNSET)

        fixed_rate_subtotal_val = d.pop("fixed_rate_subtotal_val", UNSET)

        fixed_rate_subtotal_vol = d.pop("fixed_rate_subtotal_vol", UNSET)

        floating_rate_1y_or_below_val = d.pop("floating_rate_1y_or_below_val", UNSET)

        floating_rate_1y_or_below_vol = d.pop("floating_rate_1y_or_below_vol", UNSET)

        floating_rate_1yto3y_val = d.pop("floating_rate_1yto3y_val", UNSET)

        floating_rate_1yto3y_vol = d.pop("floating_rate_1yto3y_vol", UNSET)

        floating_rate_3yto5y_val = d.pop("floating_rate_3yto5y_val", UNSET)

        floating_rate_3yto5y_vol = d.pop("floating_rate_3yto5y_vol", UNSET)

        floating_rate_5yto7y_val = d.pop("floating_rate_5yto7y_val", UNSET)

        floating_rate_5yto7y_vol = d.pop("floating_rate_5yto7y_vol", UNSET)

        floating_rate_7y_val = d.pop("floating_rate_7y_val", UNSET)

        floating_rate_7y_vol = d.pop("floating_rate_7y_vol", UNSET)

        floating_rate_subtotal_val = d.pop("floating_rate_subtotal_val", UNSET)

        floating_rate_subtotal_vol = d.pop("floating_rate_subtotal_vol", UNSET)

        total_val = d.pop("total_val", UNSET)

        total_vol = d.pop("total_vol", UNSET)

        record = cls(
            end_of_month=end_of_month,
            fixed_rate_1y_or_below_val=fixed_rate_1y_or_below_val,
            fixed_rate_1y_or_below_vol=fixed_rate_1y_or_below_vol,
            fixed_rate_1yto3y_val=fixed_rate_1yto3y_val,
            fixed_rate_1yto3y_vol=fixed_rate_1yto3y_vol,
            fixed_rate_3yto5y_val=fixed_rate_3yto5y_val,
            fixed_rate_3yto5y_vol=fixed_rate_3yto5y_vol,
            fixed_rate_5yto7y_val=fixed_rate_5yto7y_val,
            fixed_rate_5yto7y_vol=fixed_rate_5yto7y_vol,
            fixed_rate_7y_val=fixed_rate_7y_val,
            fixed_rate_7y_vol=fixed_rate_7y_vol,
            fixed_rate_subtotal_val=fixed_rate_subtotal_val,
            fixed_rate_subtotal_vol=fixed_rate_subtotal_vol,
            floating_rate_1y_or_below_val=floating_rate_1y_or_below_val,
            floating_rate_1y_or_below_vol=floating_rate_1y_or_below_vol,
            floating_rate_1yto3y_val=floating_rate_1yto3y_val,
            floating_rate_1yto3y_vol=floating_rate_1yto3y_vol,
            floating_rate_3yto5y_val=floating_rate_3yto5y_val,
            floating_rate_3yto5y_vol=floating_rate_3yto5y_vol,
            floating_rate_5yto7y_val=floating_rate_5yto7y_val,
            floating_rate_5yto7y_vol=floating_rate_5yto7y_vol,
            floating_rate_7y_val=floating_rate_7y_val,
            floating_rate_7y_vol=floating_rate_7y_vol,
            floating_rate_subtotal_val=floating_rate_subtotal_val,
            floating_rate_subtotal_vol=floating_rate_subtotal_vol,
            total_val=total_val,
            total_vol=total_vol,
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
