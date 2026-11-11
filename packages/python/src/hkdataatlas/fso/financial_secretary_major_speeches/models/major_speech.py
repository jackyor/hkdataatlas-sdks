from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MajorSpeech")


@_attrs_define
class MajorSpeech:
    """API record fields documented for a major speech. The source does not specify the outer response envelope.

    Attributes:
        date (str): Date (D.M.YYYY)
        description (str): Content of the Major Speeches
        link (str): URL of headline
        title (str): Headline of Major Speeches
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

        major_speech = cls(
            date=date,
            description=description,
            link=link,
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
