from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StopRoute")


@_attrs_define
class StopRoute:
    """
    Attributes:
        name_en (str | Unset): English stop name in the route.
        name_sc (str | Unset): Simplified Chinese stop name in the route.
        name_tc (str | Unset): Traditional Chinese stop name in the route.
        route_id (int | Unset): Route ID.
        route_seq (int | Unset): Route sequence.
        stop_seq (int | Unset): Stop sequence under the route.
    """

    name_en: str | Unset = UNSET
    name_sc: str | Unset = UNSET
    name_tc: str | Unset = UNSET
    route_id: int | Unset = UNSET
    route_seq: int | Unset = UNSET
    stop_seq: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_en = self.name_en

        name_sc = self.name_sc

        name_tc = self.name_tc

        route_id = self.route_id

        route_seq = self.route_seq

        stop_seq = self.stop_seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if name_sc is not UNSET:
            field_dict["name_sc"] = name_sc
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc
        if route_id is not UNSET:
            field_dict["route_id"] = route_id
        if route_seq is not UNSET:
            field_dict["route_seq"] = route_seq
        if stop_seq is not UNSET:
            field_dict["stop_seq"] = stop_seq

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name_en = d.pop("name_en", UNSET)

        name_sc = d.pop("name_sc", UNSET)

        name_tc = d.pop("name_tc", UNSET)

        route_id = d.pop("route_id", UNSET)

        route_seq = d.pop("route_seq", UNSET)

        stop_seq = d.pop("stop_seq", UNSET)

        stop_route = cls(
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            route_id=route_id,
            route_seq=route_seq,
            stop_seq=stop_seq,
        )

        stop_route.additional_properties = d
        return stop_route

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
