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
        efb_7d (float | Unset):
        efb_30d (float | Unset):
        efb_91d (float | Unset):
        efb_182 (float | Unset):
        efb_273d (float | Unset):
        efb_364d (float | Unset):
        efn_2y (float | Unset):
        efn_3y (float | Unset):
        efn_4y (float | Unset):
        efn_5y (float | Unset):
        efn_7y (float | Unset):
        efn_10y (float | Unset):
        efn_15y (float | Unset):
    """

    end_of_day: datetime.date | Unset = UNSET
    efb_7d: float | Unset = UNSET
    efb_30d: float | Unset = UNSET
    efb_91d: float | Unset = UNSET
    efb_182: float | Unset = UNSET
    efb_273d: float | Unset = UNSET
    efb_364d: float | Unset = UNSET
    efn_2y: float | Unset = UNSET
    efn_3y: float | Unset = UNSET
    efn_4y: float | Unset = UNSET
    efn_5y: float | Unset = UNSET
    efn_7y: float | Unset = UNSET
    efn_10y: float | Unset = UNSET
    efn_15y: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_day: str | Unset = UNSET
        if not isinstance(self.end_of_day, Unset):
            end_of_day = self.end_of_day.isoformat()

        efb_7d = self.efb_7d

        efb_30d = self.efb_30d

        efb_91d = self.efb_91d

        efb_182 = self.efb_182

        efb_273d = self.efb_273d

        efb_364d = self.efb_364d

        efn_2y = self.efn_2y

        efn_3y = self.efn_3y

        efn_4y = self.efn_4y

        efn_5y = self.efn_5y

        efn_7y = self.efn_7y

        efn_10y = self.efn_10y

        efn_15y = self.efn_15y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_day is not UNSET:
            field_dict["end_of_day"] = end_of_day
        if efb_7d is not UNSET:
            field_dict["efb_7d"] = efb_7d
        if efb_30d is not UNSET:
            field_dict["efb_30d"] = efb_30d
        if efb_91d is not UNSET:
            field_dict["efb_91d"] = efb_91d
        if efb_182 is not UNSET:
            field_dict["efb_182"] = efb_182
        if efb_273d is not UNSET:
            field_dict["efb_273d"] = efb_273d
        if efb_364d is not UNSET:
            field_dict["efb_364d"] = efb_364d
        if efn_2y is not UNSET:
            field_dict["efn_2y"] = efn_2y
        if efn_3y is not UNSET:
            field_dict["efn_3y"] = efn_3y
        if efn_4y is not UNSET:
            field_dict["efn_4y"] = efn_4y
        if efn_5y is not UNSET:
            field_dict["efn_5y"] = efn_5y
        if efn_7y is not UNSET:
            field_dict["efn_7y"] = efn_7y
        if efn_10y is not UNSET:
            field_dict["efn_10y"] = efn_10y
        if efn_15y is not UNSET:
            field_dict["efn_15y"] = efn_15y

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

        efb_7d = d.pop("efb_7d", UNSET)

        efb_30d = d.pop("efb_30d", UNSET)

        efb_91d = d.pop("efb_91d", UNSET)

        efb_182 = d.pop("efb_182", UNSET)

        efb_273d = d.pop("efb_273d", UNSET)

        efb_364d = d.pop("efb_364d", UNSET)

        efn_2y = d.pop("efn_2y", UNSET)

        efn_3y = d.pop("efn_3y", UNSET)

        efn_4y = d.pop("efn_4y", UNSET)

        efn_5y = d.pop("efn_5y", UNSET)

        efn_7y = d.pop("efn_7y", UNSET)

        efn_10y = d.pop("efn_10y", UNSET)

        efn_15y = d.pop("efn_15y", UNSET)

        record = cls(
            end_of_day=end_of_day,
            efb_7d=efb_7d,
            efb_30d=efb_30d,
            efb_91d=efb_91d,
            efb_182=efb_182,
            efb_273d=efb_273d,
            efb_364d=efb_364d,
            efn_2y=efn_2y,
            efn_3y=efn_3y,
            efn_4y=efn_4y,
            efn_5y=efn_5y,
            efn_7y=efn_7y,
            efn_10y=efn_10y,
            efn_15y=efn_15y,
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
