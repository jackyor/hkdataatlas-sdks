from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.route_bound import RouteBound, check_route_bound
from ..types import UNSET, Unset

T = TypeVar("T", bound="Route")


@_attrs_define
class Route:
    """An empty data object denotes data not available.

    Attributes:
        bound (RouteBound | Unset): Route direction: I is inbound and O is outbound. Example: O.
        co (str | Unset): Bus company. The value is documented as KMB, including bus route services of KMB and LWB.
            Example: KMB.
        data_timestamp (datetime.datetime | Unset): Date-time timestamp with time zone in ISO 8601 format.
        dest_en (str | Unset): Route destination in English.
        dest_sc (str | Unset): Route destination in Simplified Chinese.
        dest_tc (str | Unset): Route destination in Traditional Chinese.
        orig_en (str | Unset): Route origin in English.
        orig_sc (str | Unset): Route origin in Simplified Chinese.
        orig_tc (str | Unset): Route origin in Traditional Chinese.
        route (str | Unset): Bus route number; route services of KMB and LWB are included. Example: 74B.
        service_type (str | Unset): Service type of the bus route. Example: 1.
    """

    bound: RouteBound | Unset = UNSET
    co: str | Unset = UNSET
    data_timestamp: datetime.datetime | Unset = UNSET
    dest_en: str | Unset = UNSET
    dest_sc: str | Unset = UNSET
    dest_tc: str | Unset = UNSET
    orig_en: str | Unset = UNSET
    orig_sc: str | Unset = UNSET
    orig_tc: str | Unset = UNSET
    route: str | Unset = UNSET
    service_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bound: str | Unset = UNSET
        if not isinstance(self.bound, Unset):
            bound = self.bound

        co = self.co

        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        dest_en = self.dest_en

        dest_sc = self.dest_sc

        dest_tc = self.dest_tc

        orig_en = self.orig_en

        orig_sc = self.orig_sc

        orig_tc = self.orig_tc

        route = self.route

        service_type = self.service_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bound is not UNSET:
            field_dict["bound"] = bound
        if co is not UNSET:
            field_dict["co"] = co
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if dest_en is not UNSET:
            field_dict["dest_en"] = dest_en
        if dest_sc is not UNSET:
            field_dict["dest_sc"] = dest_sc
        if dest_tc is not UNSET:
            field_dict["dest_tc"] = dest_tc
        if orig_en is not UNSET:
            field_dict["orig_en"] = orig_en
        if orig_sc is not UNSET:
            field_dict["orig_sc"] = orig_sc
        if orig_tc is not UNSET:
            field_dict["orig_tc"] = orig_tc
        if route is not UNSET:
            field_dict["route"] = route
        if service_type is not UNSET:
            field_dict["service_type"] = service_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _bound = d.pop("bound", UNSET)
        bound: RouteBound | Unset
        if isinstance(_bound, Unset):
            bound = UNSET
        else:
            bound = check_route_bound(_bound)

        co = d.pop("co", UNSET)

        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        dest_en = d.pop("dest_en", UNSET)

        dest_sc = d.pop("dest_sc", UNSET)

        dest_tc = d.pop("dest_tc", UNSET)

        orig_en = d.pop("orig_en", UNSET)

        orig_sc = d.pop("orig_sc", UNSET)

        orig_tc = d.pop("orig_tc", UNSET)

        route = d.pop("route", UNSET)

        service_type = d.pop("service_type", UNSET)

        route = cls(
            bound=bound,
            co=co,
            data_timestamp=data_timestamp,
            dest_en=dest_en,
            dest_sc=dest_sc,
            dest_tc=dest_tc,
            orig_en=orig_en,
            orig_sc=orig_sc,
            orig_tc=orig_tc,
            route=route,
            service_type=service_type,
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
