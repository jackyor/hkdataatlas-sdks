from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PressRelease")


@_attrs_define
class PressRelease:
    """Press release fields documented for the JSON API.

    Attributes:
        date (str): Publication date. The API dictionary labels this field Date but does not specify its representation.
            The separate XML dictionary gives pubDate in D.M.YYYY format; that XML field is not the API field name.
        description (str): Content of the press release.
        link (str): URL of the headline.
        title (str): Headline of the press release.
    """

    date: str
    description: str
    link: str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        description = self.description

        link = self.link

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "description": description,
                "link": link,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("date")

        description = d.pop("description")

        link = d.pop("link")

        title = d.pop("title")

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
