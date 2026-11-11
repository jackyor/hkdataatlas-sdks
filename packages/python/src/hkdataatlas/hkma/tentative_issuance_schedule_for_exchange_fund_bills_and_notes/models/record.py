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
        tender_date (datetime.date | Unset):
        t_issue_date (datetime.date | Unset):
        tender_size (str | Unset):
        issue_type (str | Unset):
    """

    tender_date: datetime.date | Unset = UNSET
    t_issue_date: datetime.date | Unset = UNSET
    tender_size: str | Unset = UNSET
    issue_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tender_date: str | Unset = UNSET
        if not isinstance(self.tender_date, Unset):
            tender_date = self.tender_date.isoformat()

        t_issue_date: str | Unset = UNSET
        if not isinstance(self.t_issue_date, Unset):
            t_issue_date = self.t_issue_date.isoformat()

        tender_size = self.tender_size

        issue_type = self.issue_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tender_date is not UNSET:
            field_dict["tender_date"] = tender_date
        if t_issue_date is not UNSET:
            field_dict["t_issue_date"] = t_issue_date
        if tender_size is not UNSET:
            field_dict["tender_size"] = tender_size
        if issue_type is not UNSET:
            field_dict["issue_type"] = issue_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _tender_date = d.pop("tender_date", UNSET)
        tender_date: datetime.date | Unset
        if isinstance(_tender_date, Unset):
            tender_date = UNSET
        else:
            tender_date = datetime.date.fromisoformat(_tender_date)

        _t_issue_date = d.pop("t_issue_date", UNSET)
        t_issue_date: datetime.date | Unset
        if isinstance(_t_issue_date, Unset):
            t_issue_date = UNSET
        else:
            t_issue_date = datetime.date.fromisoformat(_t_issue_date)

        tender_size = d.pop("tender_size", UNSET)

        issue_type = d.pop("issue_type", UNSET)

        record = cls(
            tender_date=tender_date,
            t_issue_date=t_issue_date,
            tender_size=tender_size,
            issue_type=issue_type,
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
