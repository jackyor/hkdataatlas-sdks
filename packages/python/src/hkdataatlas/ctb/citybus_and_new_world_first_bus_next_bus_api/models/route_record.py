from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteRecord")


@_attrs_define
class RouteRecord:
    """
    Attributes:
        co (str | Unset):
        route (str | Unset):
        orig_en (str | Unset):
        orig_tc (str | Unset):
        orig_sc (str | Unset):
        dest_en (str | Unset):
        dest_tc (str | Unset):
        dest_sc (str | Unset):
        data_timestamp (str | Unset): ISO 8601 date time with time zone per dictionary; no stronger lexical restriction
            inferred.
    """

    co: str | Unset = UNSET
    route: str | Unset = UNSET
    orig_en: str | Unset = UNSET
    orig_tc: str | Unset = UNSET
    orig_sc: str | Unset = UNSET
    dest_en: str | Unset = UNSET
    dest_tc: str | Unset = UNSET
    dest_sc: str | Unset = UNSET
    data_timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co = self.co

        route = self.route

        orig_en = self.orig_en

        orig_tc = self.orig_tc

        orig_sc = self.orig_sc

        dest_en = self.dest_en

        dest_tc = self.dest_tc

        dest_sc = self.dest_sc

        data_timestamp = self.data_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co is not UNSET:
            field_dict["co"] = co
        if route is not UNSET:
            field_dict["route"] = route
        if orig_en is not UNSET:
            field_dict["orig_en"] = orig_en
        if orig_tc is not UNSET:
            field_dict["orig_tc"] = orig_tc
        if orig_sc is not UNSET:
            field_dict["orig_sc"] = orig_sc
        if dest_en is not UNSET:
            field_dict["dest_en"] = dest_en
        if dest_tc is not UNSET:
            field_dict["dest_tc"] = dest_tc
        if dest_sc is not UNSET:
            field_dict["dest_sc"] = dest_sc
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        co = d.pop("co", UNSET)

        route = d.pop("route", UNSET)

        orig_en = d.pop("orig_en", UNSET)

        orig_tc = d.pop("orig_tc", UNSET)

        orig_sc = d.pop("orig_sc", UNSET)

        dest_en = d.pop("dest_en", UNSET)

        dest_tc = d.pop("dest_tc", UNSET)

        dest_sc = d.pop("dest_sc", UNSET)

        data_timestamp = d.pop("data_timestamp", UNSET)

        route_record = cls(
            co=co,
            route=route,
            orig_en=orig_en,
            orig_tc=orig_tc,
            orig_sc=orig_sc,
            dest_en=dest_en,
            dest_tc=dest_tc,
            dest_sc=dest_sc,
            data_timestamp=data_timestamp,
        )

        route_record.additional_properties = d
        return route_record

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
