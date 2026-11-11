from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeatStressAtWorkWarning")


@_attrs_define
class HeatStressAtWorkWarning:
    """Heat Stress at Work Warning object.

    Attributes:
        action_code (str | Unset): Action code. The documented values are ISSUE and CANCEL.
        desc (str | Unset): Warning description.
        effective_time (datetime.datetime | Unset): Effective time in the format YYYY-MM-DD'T'HH:mm:ssZ.
        issue_time (datetime.datetime | Unset): Issue time in the format YYYY-MM-DD'T'HH:mm:ssZ.
        warning_level (str | Unset): Warning level. The documented code listing includes AMBER, RED, and BLACK. The
            cancellation example has an empty string; the source does not state whether these codes exhaust all possible
            values.
    """

    action_code: str | Unset = UNSET
    desc: str | Unset = UNSET
    effective_time: datetime.datetime | Unset = UNSET
    issue_time: datetime.datetime | Unset = UNSET
    warning_level: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_code = self.action_code

        desc = self.desc

        effective_time: str | Unset = UNSET
        if not isinstance(self.effective_time, Unset):
            effective_time = self.effective_time.isoformat()

        issue_time: str | Unset = UNSET
        if not isinstance(self.issue_time, Unset):
            issue_time = self.issue_time.isoformat()

        warning_level = self.warning_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_code is not UNSET:
            field_dict["actionCode"] = action_code
        if desc is not UNSET:
            field_dict["desc"] = desc
        if effective_time is not UNSET:
            field_dict["effectiveTime"] = effective_time
        if issue_time is not UNSET:
            field_dict["issueTime"] = issue_time
        if warning_level is not UNSET:
            field_dict["warningLevel"] = warning_level

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        action_code = d.pop("actionCode", UNSET)

        desc = d.pop("desc", UNSET)

        _effective_time = d.pop("effectiveTime", UNSET)
        effective_time: datetime.datetime | Unset
        if isinstance(_effective_time, Unset):
            effective_time = UNSET
        else:
            effective_time = datetime.datetime.fromisoformat(_effective_time)

        _issue_time = d.pop("issueTime", UNSET)
        issue_time: datetime.datetime | Unset
        if isinstance(_issue_time, Unset):
            issue_time = UNSET
        else:
            issue_time = datetime.datetime.fromisoformat(_issue_time)

        warning_level = d.pop("warningLevel", UNSET)

        heat_stress_at_work_warning = cls(
            action_code=action_code,
            desc=desc,
            effective_time=effective_time,
            issue_time=issue_time,
            warning_level=warning_level,
        )

        heat_stress_at_work_warning.additional_properties = d
        return heat_stress_at_work_warning

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
