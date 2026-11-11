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
        hkd_fer_spot (float | Unset):
        hkd_fer_1w (float | Unset):
        hkd_fer_1m (float | Unset):
        hkd_fer_3m (float | Unset):
        hkd_fer_6m (float | Unset):
        hkd_fer_9m (float | Unset):
        hkd_fer_12m (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    hkd_fer_spot: float | Unset = UNSET
    hkd_fer_1w: float | Unset = UNSET
    hkd_fer_1m: float | Unset = UNSET
    hkd_fer_3m: float | Unset = UNSET
    hkd_fer_6m: float | Unset = UNSET
    hkd_fer_9m: float | Unset = UNSET
    hkd_fer_12m: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        hkd_fer_spot = self.hkd_fer_spot

        hkd_fer_1w = self.hkd_fer_1w

        hkd_fer_1m = self.hkd_fer_1m

        hkd_fer_3m = self.hkd_fer_3m

        hkd_fer_6m = self.hkd_fer_6m

        hkd_fer_9m = self.hkd_fer_9m

        hkd_fer_12m = self.hkd_fer_12m

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if hkd_fer_spot is not UNSET:
            field_dict["hkd_fer_spot"] = hkd_fer_spot
        if hkd_fer_1w is not UNSET:
            field_dict["hkd_fer_1w"] = hkd_fer_1w
        if hkd_fer_1m is not UNSET:
            field_dict["hkd_fer_1m"] = hkd_fer_1m
        if hkd_fer_3m is not UNSET:
            field_dict["hkd_fer_3m"] = hkd_fer_3m
        if hkd_fer_6m is not UNSET:
            field_dict["hkd_fer_6m"] = hkd_fer_6m
        if hkd_fer_9m is not UNSET:
            field_dict["hkd_fer_9m"] = hkd_fer_9m
        if hkd_fer_12m is not UNSET:
            field_dict["hkd_fer_12m"] = hkd_fer_12m

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

        hkd_fer_spot = d.pop("hkd_fer_spot", UNSET)

        hkd_fer_1w = d.pop("hkd_fer_1w", UNSET)

        hkd_fer_1m = d.pop("hkd_fer_1m", UNSET)

        hkd_fer_3m = d.pop("hkd_fer_3m", UNSET)

        hkd_fer_6m = d.pop("hkd_fer_6m", UNSET)

        hkd_fer_9m = d.pop("hkd_fer_9m", UNSET)

        hkd_fer_12m = d.pop("hkd_fer_12m", UNSET)

        record = cls(
            end_of_month=end_of_month,
            hkd_fer_spot=hkd_fer_spot,
            hkd_fer_1w=hkd_fer_1w,
            hkd_fer_1m=hkd_fer_1m,
            hkd_fer_3m=hkd_fer_3m,
            hkd_fer_6m=hkd_fer_6m,
            hkd_fer_9m=hkd_fer_9m,
            hkd_fer_12m=hkd_fer_12m,
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
