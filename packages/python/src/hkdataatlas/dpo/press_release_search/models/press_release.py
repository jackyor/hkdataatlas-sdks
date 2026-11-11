from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PressRelease")


@_attrs_define
class PressRelease:
    """A press release result as illustrated by the publisher's response example.

    Attributes:
        date (str | Unset): Publication date, shown in the example as day.month.year.
        description (str | Unset): Press release description or excerpt.
        link (str | Unset): Link to the press release. The retained current-source response also uses relative links.
            Plainstrings preserve absolute and relative publisherlinks without an unsupported absoluteURI constraint.
        title (str | Unset): Press release title.
    """

    date: str | Unset = UNSET
    description: str | Unset = UNSET
    link: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        description = self.description

        link = self.link

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if link is not UNSET:
            field_dict["link"] = link
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        link = d.pop("link", UNSET)

        title = d.pop("title", UNSET)

        press_release = cls(
            date=date,
            description=description,
            link=link,
            title=title,
        )

        press_release.additional_properties = d
        return press_release

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
