from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MajorSpeechXmlFeedRecord")


@_attrs_define
class MajorSpeechXmlFeedRecord:
    """Fields from the publisher separate XML-feed column; this does not establish XML media support at the JSON search API
    URL. Catalogued XML feeds are separate URLs.

        Attributes:
            link (str): URL of the headline.
            pub_date (str): Publication date, documented in D.M.YYYY format.
            title (str): Headline of the major speech.
    """

    link: str
    pub_date: str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link = self.link

        pub_date = self.pub_date

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link": link,
                "pubDate": pub_date,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        link = d.pop("link")

        pub_date = d.pop("pubDate")

        title = d.pop("title")

        major_speech_xml_feed_record = cls(
            link=link,
            pub_date=pub_date,
            title=title,
        )

        major_speech_xml_feed_record.additional_properties = d
        return major_speech_xml_feed_record

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
