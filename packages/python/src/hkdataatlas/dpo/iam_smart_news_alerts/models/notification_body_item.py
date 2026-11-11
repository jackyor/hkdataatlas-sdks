from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_body_item_type import (
    NotificationBodyItemType,
    check_notification_body_item_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationBodyItem")


@_attrs_define
class NotificationBodyItem:
    """A content item. For P (text), alt is not applicable and val is text content. For I (image), alt is an image
    description and val is an image URL. For A (URL), alt is a link description and val is a link URL.

        Attributes:
            alt (str | Unset):
            type_ (NotificationBodyItemType | Unset):
            val (str | Unset):
    """

    alt: str | Unset = UNSET
    type_: NotificationBodyItemType | Unset = UNSET
    val: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alt = self.alt

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        val = self.val

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alt is not UNSET:
            field_dict["alt"] = alt
        if type_ is not UNSET:
            field_dict["type"] = type_
        if val is not UNSET:
            field_dict["val"] = val

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alt = d.pop("alt", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: NotificationBodyItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_notification_body_item_type(_type_)

        val = d.pop("val", UNSET)

        notification_body_item = cls(
            alt=alt,
            type_=type_,
            val=val,
        )

        notification_body_item.additional_properties = d
        return notification_body_item

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
