from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Route")


@_attrs_define
class Route:
    """
    Attributes:
        overnight_route (int | Unset): Indicates whether the route is an overnight route: 1 if yes, otherwise 0.
        route_id (int | str | Unset): Declared as Integer; the documented sample represents the identifier as a string.
        route_name_c (str | Unset):
        route_name_e (str | Unset):
        route_name_s (str | Unset):
        route_no (str | Unset):
        special_route (int | Unset): Indicates whether the route is a special route: 1 if yes, otherwise 0.
    """

    overnight_route: int | Unset = UNSET
    route_id: int | str | Unset = UNSET
    route_name_c: str | Unset = UNSET
    route_name_e: str | Unset = UNSET
    route_name_s: str | Unset = UNSET
    route_no: str | Unset = UNSET
    special_route: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overnight_route = self.overnight_route

        route_id: int | str | Unset
        if isinstance(self.route_id, Unset):
            route_id = UNSET
        else:
            route_id = self.route_id

        route_name_c = self.route_name_c

        route_name_e = self.route_name_e

        route_name_s = self.route_name_s

        route_no = self.route_no

        special_route = self.special_route

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if overnight_route is not UNSET:
            field_dict["overnightRoute"] = overnight_route
        if route_id is not UNSET:
            field_dict["routeId"] = route_id
        if route_name_c is not UNSET:
            field_dict["routeName_c"] = route_name_c
        if route_name_e is not UNSET:
            field_dict["routeName_e"] = route_name_e
        if route_name_s is not UNSET:
            field_dict["routeName_s"] = route_name_s
        if route_no is not UNSET:
            field_dict["routeNo"] = route_no
        if special_route is not UNSET:
            field_dict["specialRoute"] = special_route

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        overnight_route = d.pop("overnightRoute", UNSET)

        def _parse_route_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        route_id = _parse_route_id(d.pop("routeId", UNSET))

        route_name_c = d.pop("routeName_c", UNSET)

        route_name_e = d.pop("routeName_e", UNSET)

        route_name_s = d.pop("routeName_s", UNSET)

        route_no = d.pop("routeNo", UNSET)

        special_route = d.pop("specialRoute", UNSET)

        route = cls(
            overnight_route=overnight_route,
            route_id=route_id,
            route_name_c=route_name_c,
            route_name_e=route_name_e,
            route_name_s=route_name_s,
            route_no=route_no,
            special_route=special_route,
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
