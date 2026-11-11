from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenderNotice")


@_attrs_define
class TenderNotice:
    """A tender notice record.

    Attributes:
        file_link (str | Unset): URL of the tender file.
        post_date (str | Unset): Posting date of the tender.
        title (str | Unset): Title of the tender.
    """

    file_link: str | Unset = UNSET
    post_date: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_link = self.file_link

        post_date = self.post_date

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_link is not UNSET:
            field_dict["file_link"] = file_link
        if post_date is not UNSET:
            field_dict["post_date"] = post_date
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        file_link = d.pop("file_link", UNSET)

        post_date = d.pop("post_date", UNSET)

        title = d.pop("title", UNSET)

        tender_notice = cls(
            file_link=file_link,
            post_date=post_date,
            title=title,
        )

        tender_notice.additional_properties = d
        return tender_notice

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
