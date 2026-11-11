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
        end_of_day (datetime.date | Unset):
        ir_overnight (float | Unset):
        ir_1w (float | Unset):
        ir_1m (float | Unset):
        ir_3m (float | Unset):
        ir_6m (float | Unset):
        ir_9m (float | Unset):
        ir_12m (float | Unset):
    """

    end_of_day: datetime.date | Unset = UNSET
    ir_overnight: float | Unset = UNSET
    ir_1w: float | Unset = UNSET
    ir_1m: float | Unset = UNSET
    ir_3m: float | Unset = UNSET
    ir_6m: float | Unset = UNSET
    ir_9m: float | Unset = UNSET
    ir_12m: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_day: str | Unset = UNSET
        if not isinstance(self.end_of_day, Unset):
            end_of_day = self.end_of_day.isoformat()

        ir_overnight = self.ir_overnight

        ir_1w = self.ir_1w

        ir_1m = self.ir_1m

        ir_3m = self.ir_3m

        ir_6m = self.ir_6m

        ir_9m = self.ir_9m

        ir_12m = self.ir_12m

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_day is not UNSET:
            field_dict["end_of_day"] = end_of_day
        if ir_overnight is not UNSET:
            field_dict["ir_overnight"] = ir_overnight
        if ir_1w is not UNSET:
            field_dict["ir_1w"] = ir_1w
        if ir_1m is not UNSET:
            field_dict["ir_1m"] = ir_1m
        if ir_3m is not UNSET:
            field_dict["ir_3m"] = ir_3m
        if ir_6m is not UNSET:
            field_dict["ir_6m"] = ir_6m
        if ir_9m is not UNSET:
            field_dict["ir_9m"] = ir_9m
        if ir_12m is not UNSET:
            field_dict["ir_12m"] = ir_12m

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_day = d.pop("end_of_day", UNSET)
        end_of_day: datetime.date | Unset
        if isinstance(_end_of_day, Unset):
            end_of_day = UNSET
        else:
            end_of_day = datetime.date.fromisoformat(_end_of_day)

        ir_overnight = d.pop("ir_overnight", UNSET)

        ir_1w = d.pop("ir_1w", UNSET)

        ir_1m = d.pop("ir_1m", UNSET)

        ir_3m = d.pop("ir_3m", UNSET)

        ir_6m = d.pop("ir_6m", UNSET)

        ir_9m = d.pop("ir_9m", UNSET)

        ir_12m = d.pop("ir_12m", UNSET)

        record = cls(
            end_of_day=end_of_day,
            ir_overnight=ir_overnight,
            ir_1w=ir_1w,
            ir_1m=ir_1m,
            ir_3m=ir_3m,
            ir_6m=ir_6m,
            ir_9m=ir_9m,
            ir_12m=ir_12m,
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
