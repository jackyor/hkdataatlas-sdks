from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WarningSummaryEntry")


@_attrs_define
class WarningSummaryEntry:
    """
    Attributes:
        action_code (str | Unset): Action code. Documented values include ISSUE, REISSUE (for WCOLD, WHOT and WFNTSA),
            CANCEL, EXTEND (WTS) and UPDATE (WTS), with applicability depending on warning.
        code (str | Unset): Warning code or signal subtype code.
        expire_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
        issue_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
        name (str | Unset): Warning name.
        type_ (str | Unset): Warning type where supplied.
        update_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
    """

    action_code: str | Unset = UNSET
    code: str | Unset = UNSET
    expire_time: str | Unset = UNSET
    issue_time: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    update_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_code = self.action_code

        code = self.code

        expire_time = self.expire_time

        issue_time = self.issue_time

        name = self.name

        type_ = self.type_

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_code is not UNSET:
            field_dict["actionCode"] = action_code
        if code is not UNSET:
            field_dict["code"] = code
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if issue_time is not UNSET:
            field_dict["issueTime"] = issue_time
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        action_code = d.pop("actionCode", UNSET)

        code = d.pop("code", UNSET)

        expire_time = d.pop("expireTime", UNSET)

        issue_time = d.pop("issueTime", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        update_time = d.pop("updateTime", UNSET)

        warning_summary_entry = cls(
            action_code=action_code,
            code=code,
            expire_time=expire_time,
            issue_time=issue_time,
            name=name,
            type_=type_,
            update_time=update_time,
        )

        warning_summary_entry.additional_properties = d
        return warning_summary_entry

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
