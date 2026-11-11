from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulletinHeader")


@_attrs_define
class BulletinHeader:
    """
    Attributes:
        bulletin_name (str | Unset): Name of the bulletin. Plain text; static data.
        bulletin_provider (str | Unset): Provider of the bulletin. Plain text; static data.
        bulletin_time (str | Unset): Issue time of the bulletin, with the time offset indicating hours ahead of UTC. The
            dictionary gives the format {YYYY}-{MM}-{DD}T{hh}:{mm}:{ss}+{ZZ}:00 and example 2018-10-30T01:00:00+08:00.
            Example: 2018-10-30T01:00:00+08:00.
        bulletin_type (str | Unset): Type of the bulletin. One alphabet character; R represents a report type. Static
            data. Example: R.
    """

    bulletin_name: str | Unset = UNSET
    bulletin_provider: str | Unset = UNSET
    bulletin_time: str | Unset = UNSET
    bulletin_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bulletin_name = self.bulletin_name

        bulletin_provider = self.bulletin_provider

        bulletin_time = self.bulletin_time

        bulletin_type = self.bulletin_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bulletin_name is not UNSET:
            field_dict["BulletinName"] = bulletin_name
        if bulletin_provider is not UNSET:
            field_dict["BulletinProvider"] = bulletin_provider
        if bulletin_time is not UNSET:
            field_dict["BulletinTime"] = bulletin_time
        if bulletin_type is not UNSET:
            field_dict["BulletinType"] = bulletin_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bulletin_name = d.pop("BulletinName", UNSET)

        bulletin_provider = d.pop("BulletinProvider", UNSET)

        bulletin_time = d.pop("BulletinTime", UNSET)

        bulletin_type = d.pop("BulletinType", UNSET)

        bulletin_header = cls(
            bulletin_name=bulletin_name,
            bulletin_provider=bulletin_provider,
            bulletin_time=bulletin_time,
            bulletin_type=bulletin_type,
        )

        bulletin_header.additional_properties = d
        return bulletin_header

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
