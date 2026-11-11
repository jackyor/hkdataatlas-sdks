from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.routes_all_response_data_routes import RoutesAllResponseDataRoutes


T = TypeVar("T", bound="RoutesAllResponseData")


@_attrs_define
class RoutesAllResponseData:
    """
    Attributes:
        data_timestamp (datetime.datetime | Unset): Last updated timestamp of route list.
        routes (RoutesAllResponseDataRoutes | Unset): Route codes grouped by region.
    """

    data_timestamp: datetime.datetime | Unset = UNSET
    routes: RoutesAllResponseDataRoutes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        routes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.routes, Unset):
            routes = self.routes.to_dict()

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
        from ..models.routes_all_response_data_routes import RoutesAllResponseDataRoutes

        d = dict(src_dict)
        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        _routes = d.pop("routes", UNSET)
        routes: RoutesAllResponseDataRoutes | Unset
        if isinstance(_routes, Unset):
            routes = UNSET
        else:
            routes = RoutesAllResponseDataRoutes.from_dict(_routes)

        routes_all_response_data = cls(
            data_timestamp=data_timestamp,
            routes=routes,
        )

        routes_all_response_data.additional_properties = d
        return routes_all_response_data

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
