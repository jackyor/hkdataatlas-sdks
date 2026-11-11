from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.speech_article import SpeechArticle


T = TypeVar("T", bound="SearchChiefExecutiveSpeechesAndArticlesResponse200")


@_attrs_define
class SearchChiefExecutiveSpeechesAndArticlesResponse200:
    """
    Attributes:
        records (list[SpeechArticle] | Unset): Speech and article records. The response property name and envelope are
            not specified in the documentation; this is a permissive representation of the documented record structure.
    """

    records: list[SpeechArticle] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.speech_article import SpeechArticle

        d = dict(src_dict)
        _records = d.pop("records", UNSET)
        records: list[SpeechArticle] | Unset = UNSET
        if _records is not UNSET:
            records = []
            for records_item_data in _records:
                records_item = SpeechArticle.from_dict(records_item_data)

                records.append(records_item)

        search_chief_executive_speeches_and_articles_response_200 = cls(
            records=records,
        )

        search_chief_executive_speeches_and_articles_response_200.additional_properties = d
        return search_chief_executive_speeches_and_articles_response_200

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
