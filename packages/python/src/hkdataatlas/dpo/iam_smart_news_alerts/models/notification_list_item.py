from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationListItem")


@_attrs_define
class NotificationListItem:
    """Fields documented for an item in the notification list. The specification does not state field requiredness or a
    complete response envelope.

        Attributes:
            exp_ts (int | Unset): Expiry time of the notification, in milliseconds since 1 January 1970.
            id (int | str | Unset): Unique identifier of the notification. The specification does not state a wire type.
            schedule_ts (int | Unset): Effective time of the notification, in milliseconds since 1 January 1970.
            source_id (str | Unset): The first two or three letters identify the supplying organisation. These are
                documented prefixes, not complete closed identifier values; the retained detail value TD0001 is valid. Suffix
                syntax is undocumented.
            subject (str | Unset): Subject of the notification.
    """

    exp_ts: int | Unset = UNSET
    id: int | str | Unset = UNSET
    schedule_ts: int | Unset = UNSET
    source_id: str | Unset = UNSET
    subject: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exp_ts = self.exp_ts

        id: int | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        schedule_ts = self.schedule_ts

        source_id = self.source_id

        subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exp_ts is not UNSET:
            field_dict["exp_ts"] = exp_ts
        if id is not UNSET:
            field_dict["id"] = id
        if schedule_ts is not UNSET:
            field_dict["schedule_ts"] = schedule_ts
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        exp_ts = d.pop("exp_ts", UNSET)

        def _parse_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        schedule_ts = d.pop("schedule_ts", UNSET)

        source_id = d.pop("source_id", UNSET)

        subject = d.pop("subject", UNSET)

        notification_list_item = cls(
            exp_ts=exp_ts,
            id=id,
            schedule_ts=schedule_ts,
            source_id=source_id,
            subject=subject,
        )

        notification_list_item.additional_properties = d
        return notification_list_item

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
