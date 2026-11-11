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
        deposit_rate_1w (float | Unset):
        deposit_rate_1m (float | Unset):
        deposit_rate_3m (float | Unset):
        deposit_rate_6m (float | Unset):
        deposit_rate_12m (float | Unset):
        savings_deposit_rate (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    deposit_rate_1w: float | Unset = UNSET
    deposit_rate_1m: float | Unset = UNSET
    deposit_rate_3m: float | Unset = UNSET
    deposit_rate_6m: float | Unset = UNSET
    deposit_rate_12m: float | Unset = UNSET
    savings_deposit_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        deposit_rate_1w = self.deposit_rate_1w

        deposit_rate_1m = self.deposit_rate_1m

        deposit_rate_3m = self.deposit_rate_3m

        deposit_rate_6m = self.deposit_rate_6m

        deposit_rate_12m = self.deposit_rate_12m

        savings_deposit_rate = self.savings_deposit_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if deposit_rate_1w is not UNSET:
            field_dict["deposit_rate_1w"] = deposit_rate_1w
        if deposit_rate_1m is not UNSET:
            field_dict["deposit_rate_1m"] = deposit_rate_1m
        if deposit_rate_3m is not UNSET:
            field_dict["deposit_rate_3m"] = deposit_rate_3m
        if deposit_rate_6m is not UNSET:
            field_dict["deposit_rate_6m"] = deposit_rate_6m
        if deposit_rate_12m is not UNSET:
            field_dict["deposit_rate_12m"] = deposit_rate_12m
        if savings_deposit_rate is not UNSET:
            field_dict["savings_deposit_rate"] = savings_deposit_rate

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

        deposit_rate_1w = d.pop("deposit_rate_1w", UNSET)

        deposit_rate_1m = d.pop("deposit_rate_1m", UNSET)

        deposit_rate_3m = d.pop("deposit_rate_3m", UNSET)

        deposit_rate_6m = d.pop("deposit_rate_6m", UNSET)

        deposit_rate_12m = d.pop("deposit_rate_12m", UNSET)

        savings_deposit_rate = d.pop("savings_deposit_rate", UNSET)

        record = cls(
            end_of_month=end_of_month,
            deposit_rate_1w=deposit_rate_1w,
            deposit_rate_1m=deposit_rate_1m,
            deposit_rate_3m=deposit_rate_3m,
            deposit_rate_6m=deposit_rate_6m,
            deposit_rate_12m=deposit_rate_12m,
            savings_deposit_rate=savings_deposit_rate,
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
