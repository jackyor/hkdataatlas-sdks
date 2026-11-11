from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.route_stop_bound import RouteStopBound, check_route_stop_bound
from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteStop")


@_attrs_define
class RouteStop:
    """
    Attributes:
        bound (RouteStopBound | Unset): Route direction: I is inbound and O is outbound. Example: O.
        co (str | Unset): Bus company; documented value is KMB. Example: KMB.
        data_timestamp (datetime.datetime | Unset): Date-time timestamp with time zone in ISO 8601 format.
        route (str | Unset): Bus route number. Example: 1A.
        seq (int | str | Unset): Stop sequence number of a bus route. The publisher declares Numeric and shows numeric
            examples. One retained documented route-stop response contains 35 string seq values; this observed runtime
            discrepancy is represented alongside the declared integer type, without claiming a universal encoding. Example:
            1.
        service_type (str | Unset): Service type of the bus route. The dictionary declares String; ETA examples
            elsewhere show numeric service_type values. Example: 1.
        stop (str | Unset): ID of a bus stop. Example: A3ADFCDF8487ADB9.
    """

    bound: RouteStopBound | Unset = UNSET
    co: str | Unset = UNSET
    data_timestamp: datetime.datetime | Unset = UNSET
    route: str | Unset = UNSET
    seq: int | str | Unset = UNSET
    service_type: str | Unset = UNSET
    stop: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bound: str | Unset = UNSET
        if not isinstance(self.bound, Unset):
            bound = self.bound

        co = self.co

        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        route = self.route

        seq: int | str | Unset
        if isinstance(self.seq, Unset):
            seq = UNSET
        else:
            seq = self.seq

        service_type = self.service_type

        stop = self.stop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bound is not UNSET:
            field_dict["bound"] = bound
        if co is not UNSET:
            field_dict["co"] = co
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if route is not UNSET:
            field_dict["route"] = route
        if seq is not UNSET:
            field_dict["seq"] = seq
        if service_type is not UNSET:
            field_dict["service_type"] = service_type
        if stop is not UNSET:
            field_dict["stop"] = stop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _bound = d.pop("bound", UNSET)
        bound: RouteStopBound | Unset
        if isinstance(_bound, Unset):
            bound = UNSET
        else:
            bound = check_route_stop_bound(_bound)

        co = d.pop("co", UNSET)

        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        route = d.pop("route", UNSET)

        def _parse_seq(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        seq = _parse_seq(d.pop("seq", UNSET))

        service_type = d.pop("service_type", UNSET)

        stop = d.pop("stop", UNSET)

        route_stop = cls(
            bound=bound,
            co=co,
            data_timestamp=data_timestamp,
            route=route,
            seq=seq,
            service_type=service_type,
            stop=stop,
        )

        route_stop.additional_properties = d
        return route_stop

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
