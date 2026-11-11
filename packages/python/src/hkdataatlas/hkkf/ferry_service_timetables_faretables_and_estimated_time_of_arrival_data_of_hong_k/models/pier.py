from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pier")


@_attrs_define
class Pier:
    """
    Attributes:
        lat (float | Unset): Latitude of a pier location. Example: 22.22652.
        long (float | Unset): Longitude of a pier location. Example: 114.109105.
        name_en (str | Unset): Pier name in English. Example: Yung Shue Wan Pier.
        name_sc (str | Unset): Pier name in Simplified Chinese. Example: 榕树湾渡轮码头.
        name_tc (str | Unset): Pier name in Traditional Chinese. Example: 榕樹灣渡輪碼頭.
        pier_id (int | str | Unset): Pier ID. The companion dictionary declares String; the primary API response sample
            represents it as a number.
    """

    lat: float | Unset = UNSET
    long: float | Unset = UNSET
    name_en: str | Unset = UNSET
    name_sc: str | Unset = UNSET
    name_tc: str | Unset = UNSET
    pier_id: int | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lat = self.lat

        long = self.long

        name_en = self.name_en

        name_sc = self.name_sc

        name_tc = self.name_tc

        pier_id: int | str | Unset
        if isinstance(self.pier_id, Unset):
            pier_id = UNSET
        else:
            pier_id = self.pier_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lat is not UNSET:
            field_dict["lat"] = lat
        if long is not UNSET:
            field_dict["long"] = long
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if name_sc is not UNSET:
            field_dict["name_sc"] = name_sc
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc
        if pier_id is not UNSET:
            field_dict["pier_id"] = pier_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lat = d.pop("lat", UNSET)

        long = d.pop("long", UNSET)

        name_en = d.pop("name_en", UNSET)

        name_sc = d.pop("name_sc", UNSET)

        name_tc = d.pop("name_tc", UNSET)

        def _parse_pier_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        pier_id = _parse_pier_id(d.pop("pier_id", UNSET))

        pier = cls(
            lat=lat,
            long=long,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            pier_id=pier_id,
        )

        pier.additional_properties = d
        return pier

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
