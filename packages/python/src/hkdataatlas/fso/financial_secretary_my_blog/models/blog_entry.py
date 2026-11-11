from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BlogEntry")


@_attrs_define
class BlogEntry:
    """A My Blog entry, as documented for the API response.

    Attributes:
        description (str): My Blog content.
        link (str): URL of headline.
        pub_date (str): Publication date. The documentation gives an example such as `Sun, 24 Feb 2019 10:00:00 +0800`
            but does not specify a machine-readable date format.
        title (str): Headline of My Blog.
    """

    description: str
    link: str
    pub_date: str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        link = self.link

        pub_date = self.pub_date

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "link": link,
                "pubDate": pub_date,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description")

        link = d.pop("link")

        pub_date = d.pop("pubDate")

        title = d.pop("title")

        blog_entry = cls(
            description=description,
            link=link,
            pub_date=pub_date,
            title=title,
        )

        blog_entry.additional_properties = d
        return blog_entry

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
