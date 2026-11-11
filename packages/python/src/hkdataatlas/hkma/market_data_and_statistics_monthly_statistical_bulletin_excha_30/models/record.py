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
        dr_1w (float | Unset):
        dr_1m (float | Unset):
        dr_3m (float | Unset):
        dr_6m (float | Unset):
        dr_12m (float | Unset):
        savings_deposit_rate (float | Unset):
        best_lending_rate (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    dr_1w: float | Unset = UNSET
    dr_1m: float | Unset = UNSET
    dr_3m: float | Unset = UNSET
    dr_6m: float | Unset = UNSET
    dr_12m: float | Unset = UNSET
    savings_deposit_rate: float | Unset = UNSET
    best_lending_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        dr_1w = self.dr_1w

        dr_1m = self.dr_1m

        dr_3m = self.dr_3m

        dr_6m = self.dr_6m

        dr_12m = self.dr_12m

        savings_deposit_rate = self.savings_deposit_rate

        best_lending_rate = self.best_lending_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if dr_1w is not UNSET:
            field_dict["dr_1w"] = dr_1w
        if dr_1m is not UNSET:
            field_dict["dr_1m"] = dr_1m
        if dr_3m is not UNSET:
            field_dict["dr_3m"] = dr_3m
        if dr_6m is not UNSET:
            field_dict["dr_6m"] = dr_6m
        if dr_12m is not UNSET:
            field_dict["dr_12m"] = dr_12m
        if savings_deposit_rate is not UNSET:
            field_dict["savings_deposit_rate"] = savings_deposit_rate
        if best_lending_rate is not UNSET:
            field_dict["best_lending_rate"] = best_lending_rate

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

        dr_1w = d.pop("dr_1w", UNSET)

        dr_1m = d.pop("dr_1m", UNSET)

        dr_3m = d.pop("dr_3m", UNSET)

        dr_6m = d.pop("dr_6m", UNSET)

        dr_12m = d.pop("dr_12m", UNSET)

        savings_deposit_rate = d.pop("savings_deposit_rate", UNSET)

        best_lending_rate = d.pop("best_lending_rate", UNSET)

        record = cls(
            end_of_month=end_of_month,
            dr_1w=dr_1w,
            dr_1m=dr_1m,
            dr_3m=dr_3m,
            dr_6m=dr_6m,
            dr_12m=dr_12m,
            savings_deposit_rate=savings_deposit_rate,
            best_lending_rate=best_lending_rate,
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
