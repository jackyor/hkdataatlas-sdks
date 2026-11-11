from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenditionUrls")


@_attrs_define
class RenditionUrls:
    """Image renditions; the property is empty/omitted when the carpark has no photo.

    Attributes:
        banner (str | Unset): Absolute image URL, 300x250 center-cropped rectangle.
        square (str | Unset): Absolute image URL, 150x150 center-cropped square.
        thumbnail (str | Unset): Absolute image URL, center-cropped rectangle, maximum 320 by 250.
    """

    banner: str | Unset = UNSET
    square: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        banner = self.banner

        square = self.square

        thumbnail = self.thumbnail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if banner is not UNSET:
            field_dict["banner"] = banner
        if square is not UNSET:
            field_dict["square"] = square
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        banner = d.pop("banner", UNSET)

        square = d.pop("square", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        rendition_urls = cls(
            banner=banner,
            square=square,
            thumbnail=thumbnail,
        )

        rendition_urls.additional_properties = d
        return rendition_urls

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
