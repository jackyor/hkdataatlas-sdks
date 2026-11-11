from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SpeechArticle")


@_attrs_define
class SpeechArticle:
    """A speech or article record, with fields documented as mandatory.

    Attributes:
        date (str): Date of the speech or article, documented in D.M.YYYY format.
        description (str): Content of the speech and article.
        link (str): Link of the speech and article.
        title (str): Heading of the speech and article.
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
                "Date": date,
                "Description": description,
                "Link": link,
                "Title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("Date")

        description = d.pop("Description")

        link = d.pop("Link")

        title = d.pop("Title")

        speech_article = cls(
            date=date,
            description=description,
            link=link,
            title=title,
        )

        speech_article.additional_properties = d
        return speech_article

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
