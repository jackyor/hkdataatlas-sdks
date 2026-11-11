from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MajorSpeech")


@_attrs_define
class MajorSpeech:
    """A major speech record as described by the XML dictionary. The dictionary lists title, link and pubDate for an item;
    the API table additionally lists title, link, date and description. The precise API response envelope and field-name
    alignment are not fully established.

        Attributes:
            date (str | Unset): Date (D.M.YYYY), as listed in the API field table.
            description (str | Unset): Content of the Major Speeches.
            link (str | Unset): URL of headline.
            pub_date (str | Unset): Date (D.M.YYYY), as listed for an XML item.
            title (str | Unset): Headline of Major Speeches.
    """

    date: str | Unset = UNSET
    description: str | Unset = UNSET
    link: str | Unset = UNSET
    pub_date: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        description = self.description

        link = self.link

        pub_date = self.pub_date

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
        if pub_date is not UNSET:
            field_dict["pubDate"] = pub_date
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        link = d.pop("link", UNSET)

        pub_date = d.pop("pubDate", UNSET)

        title = d.pop("title", UNSET)

        major_speech = cls(
            date=date,
            description=description,
            link=link,
            pub_date=pub_date,
            title=title,
        )

        major_speech.additional_properties = d
        return major_speech

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
