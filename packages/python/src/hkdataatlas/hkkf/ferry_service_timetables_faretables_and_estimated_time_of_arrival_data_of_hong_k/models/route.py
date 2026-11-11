from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Route")


@_attrs_define
class Route:
    """
    Attributes:
        destination_en (str | Unset): Route destination in English. Example: Sok Kwu Wan.
        destination_sc (str | Unset): Route destination in Simplified Chinese. Example: 索罟湾.
        destination_tc (str | Unset): Route destination in Traditional Chinese. Example: 索罟灣.
        origin_en (str | Unset): Route origin in English. Example: Central.
        origin_sc (str | Unset): Route origin in Simplified Chinese. Example: 中环.
        origin_tc (str | Unset): Route origin in Traditional Chinese. Example: 中環.
        route_id (int | str | Unset): Route ID. The companion dictionary declares String; the primary API samples
            represent IDs as numbers.
        route_name_en (str | Unset): Route name in English. Example: Central<=>Yung Shue Wan.
        route_name_sc (str | Unset): Route name in Simplified Chinese. Example: 中环往来榕树湾.
        route_name_tc (str | Unset): Route name in Traditional Chinese. Example: 中環往來榕樹灣.
    """

    destination_en: str | Unset = UNSET
    destination_sc: str | Unset = UNSET
    destination_tc: str | Unset = UNSET
    origin_en: str | Unset = UNSET
    origin_sc: str | Unset = UNSET
    origin_tc: str | Unset = UNSET
    route_id: int | str | Unset = UNSET
    route_name_en: str | Unset = UNSET
    route_name_sc: str | Unset = UNSET
    route_name_tc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_en = self.destination_en

        destination_sc = self.destination_sc

        destination_tc = self.destination_tc

        origin_en = self.origin_en

        origin_sc = self.origin_sc

        origin_tc = self.origin_tc

        route_id: int | str | Unset
        if isinstance(self.route_id, Unset):
            route_id = UNSET
        else:
            route_id = self.route_id

        route_name_en = self.route_name_en

        route_name_sc = self.route_name_sc

        route_name_tc = self.route_name_tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_en is not UNSET:
            field_dict["destination_en"] = destination_en
        if destination_sc is not UNSET:
            field_dict["destination_sc"] = destination_sc
        if destination_tc is not UNSET:
            field_dict["destination_tc"] = destination_tc
        if origin_en is not UNSET:
            field_dict["origin_en"] = origin_en
        if origin_sc is not UNSET:
            field_dict["origin_sc"] = origin_sc
        if origin_tc is not UNSET:
            field_dict["origin_tc"] = origin_tc
        if route_id is not UNSET:
            field_dict["route_id"] = route_id
        if route_name_en is not UNSET:
            field_dict["route_name_en"] = route_name_en
        if route_name_sc is not UNSET:
            field_dict["route_name_sc"] = route_name_sc
        if route_name_tc is not UNSET:
            field_dict["route_name_tc"] = route_name_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        destination_en = d.pop("destination_en", UNSET)

        destination_sc = d.pop("destination_sc", UNSET)

        destination_tc = d.pop("destination_tc", UNSET)

        origin_en = d.pop("origin_en", UNSET)

        origin_sc = d.pop("origin_sc", UNSET)

        origin_tc = d.pop("origin_tc", UNSET)

        def _parse_route_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        route_id = _parse_route_id(d.pop("route_id", UNSET))

        route_name_en = d.pop("route_name_en", UNSET)

        route_name_sc = d.pop("route_name_sc", UNSET)

        route_name_tc = d.pop("route_name_tc", UNSET)

        route = cls(
            destination_en=destination_en,
            destination_sc=destination_sc,
            destination_tc=destination_tc,
            origin_en=origin_en,
            origin_sc=origin_sc,
            origin_tc=origin_tc,
            route_id=route_id,
            route_name_en=route_name_en,
            route_name_sc=route_name_sc,
            route_name_tc=route_name_tc,
        )

        route.additional_properties = d
        return route

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
