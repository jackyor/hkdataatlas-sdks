from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteStopRecord")


@_attrs_define
class RouteStopRecord:
    """
    Attributes:
        co (str | Unset):
        route (str | Unset):
        dir_ (str | Unset):
        stop (str | Unset):
        seq (float | Unset):
        data_timestamp (str | Unset): ISO 8601 date time with time zone per dictionary; no stronger lexical restriction
            inferred.
    """

    co: str | Unset = UNSET
    route: str | Unset = UNSET
    dir_: str | Unset = UNSET
    stop: str | Unset = UNSET
    seq: float | Unset = UNSET
    data_timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co = self.co

        route = self.route

        dir_ = self.dir_

        stop = self.stop

        seq = self.seq

        data_timestamp = self.data_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co is not UNSET:
            field_dict["co"] = co
        if route is not UNSET:
            field_dict["route"] = route
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if stop is not UNSET:
            field_dict["stop"] = stop
        if seq is not UNSET:
            field_dict["seq"] = seq
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        co = d.pop("co", UNSET)

        route = d.pop("route", UNSET)

        dir_ = d.pop("dir", UNSET)

        stop = d.pop("stop", UNSET)

        seq = d.pop("seq", UNSET)

        data_timestamp = d.pop("data_timestamp", UNSET)

        route_stop_record = cls(
            co=co,
            route=route,
            dir_=dir_,
            stop=stop,
            seq=seq,
            data_timestamp=data_timestamp,
        )

        route_stop_record.additional_properties = d
        return route_stop_record

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
