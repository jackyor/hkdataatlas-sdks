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
        efb_91d (float | Unset):
        efb_182d (float | Unset):
        efb_364d (float | Unset):
        efb (float | Unset):
        efn (float | Unset):
        efbn_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    efb_91d: float | Unset = UNSET
    efb_182d: float | Unset = UNSET
    efb_364d: float | Unset = UNSET
    efb: float | Unset = UNSET
    efn: float | Unset = UNSET
    efbn_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        efb_91d = self.efb_91d

        efb_182d = self.efb_182d

        efb_364d = self.efb_364d

        efb = self.efb

        efn = self.efn

        efbn_total = self.efbn_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if efb_91d is not UNSET:
            field_dict["efb_91d"] = efb_91d
        if efb_182d is not UNSET:
            field_dict["efb_182d"] = efb_182d
        if efb_364d is not UNSET:
            field_dict["efb_364d"] = efb_364d
        if efb is not UNSET:
            field_dict["efb"] = efb
        if efn is not UNSET:
            field_dict["efn"] = efn
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

        efb_91d = d.pop("efb_91d", UNSET)

        efb_182d = d.pop("efb_182d", UNSET)

        efb_364d = d.pop("efb_364d", UNSET)

        efb = d.pop("efb", UNSET)

        efn = d.pop("efn", UNSET)

        efbn_total = d.pop("efbn_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            efb_91d=efb_91d,
            efb_182d=efb_182d,
            efb_364d=efb_364d,
            efb=efb,
            efn=efn,
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
