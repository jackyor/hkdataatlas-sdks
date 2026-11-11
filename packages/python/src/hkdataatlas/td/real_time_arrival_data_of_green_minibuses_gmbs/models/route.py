from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.direction import Direction


T = TypeVar("T", bound="Route")


@_attrs_define
class Route:
    """
    Attributes:
        data_timestamp (datetime.datetime | Unset): Last updated timestamp of route.
        description_en (str | Unset): English description of the route variation.
        description_sc (str | Unset): Simplified Chinese description of the route variation.
        description_tc (str | Unset): Traditional Chinese description of the route variation.
        directions (list[Direction] | Unset): Different directions of the variation; one-way or circular services have
            one direction.
        region (str | Unset): Region name abbreviation.
        route_code (str | Unset): Route code.
        route_id (int | Unset): Unique identifier for the route.
    """

    data_timestamp: datetime.datetime | Unset = UNSET
    description_en: str | Unset = UNSET
    description_sc: str | Unset = UNSET
    description_tc: str | Unset = UNSET
    directions: list[Direction] | Unset = UNSET
    region: str | Unset = UNSET
    route_code: str | Unset = UNSET
    route_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        description_en = self.description_en

        description_sc = self.description_sc

        description_tc = self.description_tc

        directions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.directions, Unset):
            directions = []
            for directions_item_data in self.directions:
                directions_item = directions_item_data.to_dict()
                directions.append(directions_item)

        region = self.region

        route_code = self.route_code

        route_id = self.route_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if description_en is not UNSET:
            field_dict["description_en"] = description_en
        if description_sc is not UNSET:
            field_dict["description_sc"] = description_sc
        if description_tc is not UNSET:
            field_dict["description_tc"] = description_tc
        if directions is not UNSET:
            field_dict["directions"] = directions
        if region is not UNSET:
            field_dict["region"] = region
        if route_code is not UNSET:
            field_dict["route_code"] = route_code
        if route_id is not UNSET:
            field_dict["route_id"] = route_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.direction import Direction

        d = dict(src_dict)
        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        description_en = d.pop("description_en", UNSET)

        description_sc = d.pop("description_sc", UNSET)

        description_tc = d.pop("description_tc", UNSET)

        _directions = d.pop("directions", UNSET)
        directions: list[Direction] | Unset = UNSET
        if _directions is not UNSET:
            directions = []
            for directions_item_data in _directions:
                directions_item = Direction.from_dict(directions_item_data)

                directions.append(directions_item)

        region = d.pop("region", UNSET)

        route_code = d.pop("route_code", UNSET)

        route_id = d.pop("route_id", UNSET)

        route = cls(
            data_timestamp=data_timestamp,
            description_en=description_en,
            description_sc=description_sc,
            description_tc=description_tc,
            directions=directions,
            region=region,
            route_code=route_code,
            route_id=route_id,
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
