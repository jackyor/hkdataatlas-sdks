from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchChiefSecretaryBlogResponse200")


@_attrs_define
class SearchChiefSecretaryBlogResponse200:
    """The response envelope is not specified. The documented entry fields are represented as a permissive object.

    Attributes:
        date (str | Unset): Date in D.M.YYYY format, for example 24.4.2019.
        description (str | Unset): My Blog content.
        link (str | Unset): URL of headline.
        title (str | Unset): Headline of My Blog.
    """

    date: str | Unset = UNSET
    description: str | Unset = UNSET
    link: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        description = self.description

        link = self.link

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
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        link = d.pop("link", UNSET)

        title = d.pop("title", UNSET)

        search_chief_secretary_blog_response_200 = cls(
            date=date,
            description=description,
            link=link,
            title=title,
        )

        search_chief_secretary_blog_response_200.additional_properties = d
        return search_chief_secretary_blog_response_200

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
