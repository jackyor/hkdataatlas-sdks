from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route_stop import RouteStop


T = TypeVar("T", bound="RouteStopResponseData")


@_attrs_define
class RouteStopResponseData:
    """Object holding route stops and last updated timestamp.

    Attributes:
        data_timestamp (datetime.datetime | Unset): Last updated time of route stops.
        route_stops (list[RouteStop] | Unset): Route-stop list.
    """

    data_timestamp: datetime.datetime | Unset = UNSET
    route_stops: list[RouteStop] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        route_stops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.route_stops, Unset):
            route_stops = []
            for route_stops_item_data in self.route_stops:
                route_stops_item = route_stops_item_data.to_dict()
                route_stops.append(route_stops_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if route_stops is not UNSET:
            field_dict["route_stops"] = route_stops

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.route_stop import RouteStop

        d = dict(src_dict)
        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        _route_stops = d.pop("route_stops", UNSET)
        route_stops: list[RouteStop] | Unset = UNSET
        if _route_stops is not UNSET:
            route_stops = []
            for route_stops_item_data in _route_stops:
                route_stops_item = RouteStop.from_dict(route_stops_item_data)

                route_stops.append(route_stops_item)

        route_stop_response_data = cls(
            data_timestamp=data_timestamp,
            route_stops=route_stops,
        )

        route_stop_response_data.additional_properties = d
        return route_stop_response_data

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
