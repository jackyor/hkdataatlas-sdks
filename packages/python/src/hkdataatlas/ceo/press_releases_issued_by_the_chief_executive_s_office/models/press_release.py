from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PressRelease")


@_attrs_define
class PressRelease:
    """Documented press-release fields. The source does not define additional response properties or an exhaustive object
    contract.

        Attributes:
            date (str): Date in D.M.YYYY format. Publisher table label: Date; lowercase JSON wire key observed in the saved
                response.
            description (str): Content of the Press Release. Publisher table label: Description; lowercase JSON wire key
                observed in the saved response.
            link (str): Link of the Press Release. Publisher table label: Link; lowercase JSON wire key observed in the
                saved response.
            title (str): Heading of the Press Release. Publisher table label: Title; lowercase JSON wire key observed in the
                saved response.
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
