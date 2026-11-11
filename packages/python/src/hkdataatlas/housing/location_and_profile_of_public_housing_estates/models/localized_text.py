from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalizedText")


@_attrs_define
class LocalizedText:
    """Multilingual text object shown in dictionary examples with en, zh-Hant, and zh-Hans values. The examples do not
    establish that all three properties are always present.

        Attributes:
            en (str | Unset): Value in English.
            zh_hans (str | Unset): Value in Simplified Chinese.
            zh_hant (str | Unset): Value in Traditional Chinese.
    """

    en: str | Unset = UNSET
    zh_hans: str | Unset = UNSET
    zh_hant: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en = self.en

        zh_hans = self.zh_hans

        zh_hant = self.zh_hant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en is not UNSET:
            field_dict["en"] = en
        if zh_hans is not UNSET:
            field_dict["zh-Hans"] = zh_hans
        if zh_hant is not UNSET:
            field_dict["zh-Hant"] = zh_hant

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        en = d.pop("en", UNSET)

        zh_hans = d.pop("zh-Hans", UNSET)

        zh_hant = d.pop("zh-Hant", UNSET)

        localized_text = cls(
            en=en,
            zh_hans=zh_hans,
            zh_hant=zh_hant,
        )

        localized_text.additional_properties = d
        return localized_text

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
