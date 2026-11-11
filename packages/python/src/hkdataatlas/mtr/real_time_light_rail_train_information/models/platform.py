from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route import Route


T = TypeVar("T", bound="Platform")


@_attrs_define
class Platform:
    """Information for a platform and its routes.

    Attributes:
        platform_id (int | Unset): Platform ID of each station.
        route_list (list[Route] | Unset): Array of route information for the platform.
    """

    platform_id: int | Unset = UNSET
    route_list: list[Route] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_id = self.platform_id

        route_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.route_list, Unset):
            route_list = []
            for route_list_item_data in self.route_list:
                route_list_item = route_list_item_data.to_dict()
                route_list.append(route_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform_id is not UNSET:
            field_dict["platform_id"] = platform_id
        if route_list is not UNSET:
            field_dict["route_list"] = route_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.route import Route

        d = dict(src_dict)
        platform_id = d.pop("platform_id", UNSET)

        _route_list = d.pop("route_list", UNSET)
        route_list: list[Route] | Unset = UNSET
        if _route_list is not UNSET:
            route_list = []
            for route_list_item_data in _route_list:
                route_list_item = Route.from_dict(route_list_item_data)

                route_list.append(route_list_item)

        platform = cls(
            platform_id=platform_id,
            route_list=route_list,
        )

        platform.additional_properties = d
        return platform

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
