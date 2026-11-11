from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalizedText")


@_attrs_define
class LocalizedText:
    """
    Attributes:
        en (str | Unset): English text.
        sc (str | Unset): Simplified Chinese text.
        tc (str | Unset): Traditional Chinese text.
    """

    en: str | Unset = UNSET
    sc: str | Unset = UNSET
    tc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en = self.en

        sc = self.sc

        tc = self.tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en is not UNSET:
            field_dict["en"] = en
        if sc is not UNSET:
            field_dict["sc"] = sc
        if tc is not UNSET:
            field_dict["tc"] = tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        en = d.pop("en", UNSET)

        sc = d.pop("sc", UNSET)

        tc = d.pop("tc", UNSET)

        localized_text = cls(
            en=en,
            sc=sc,
            tc=tc,
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
