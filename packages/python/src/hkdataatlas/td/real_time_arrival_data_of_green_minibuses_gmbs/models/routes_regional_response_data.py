from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoutesRegionalResponseData")


@_attrs_define
class RoutesRegionalResponseData:
    """Object holding the route-code list for the region and its last updated timestamp.

    Attributes:
        data_timestamp (datetime.datetime | Unset): The page 6 field table spells this `data.data_timstamps`; the page 7
            example uses `data_timestamp`. The sample spelling is represented here.
        routes (list[str] | Unset): Route codes for the specified region.
    """

    data_timestamp: datetime.datetime | Unset = UNSET
    routes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        routes: list[str] | Unset = UNSET
        if not isinstance(self.routes, Unset):
            routes = self.routes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if routes is not UNSET:
            field_dict["routes"] = routes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        routes = cast(list[str], d.pop("routes", UNSET))

        routes_regional_response_data = cls(
            data_timestamp=data_timestamp,
            routes=routes,
        )

        routes_regional_response_data.additional_properties = d
        return routes_regional_response_data

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
