from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alternate_route import AlternateRoute
    from ..models.route_part import RoutePart


T = TypeVar("T", bound="RouteResponse")


@_attrs_define
class RouteResponse:
    """Documented successful response fields; the sample does not establish that this object is exhaustive.

    Attributes:
        ar (list[AlternateRoute] | Unset): Alternate route information if crossing the harbour.
        cht (bool | Unset): Whether the Cross-Harbour Tunnel was used.
        dist_m (float | Unset): Total distance in metres.
        dist_u (str | Unset): Total distance with unit.
        eht (bool | Unset): Whether the Eastern Harbour Crossing was used.
        eta (str | Unset): Estimated journey time in hh:mm.
        j_speed (str | Unset): Overall average journey speed in km/h.
        route (list[RoutePart] | Unset): List of route parts.
        wht (bool | Unset): Whether the Western Harbour Crossing was used.
    """

    ar: list[AlternateRoute] | Unset = UNSET
    cht: bool | Unset = UNSET
    dist_m: float | Unset = UNSET
    dist_u: str | Unset = UNSET
    eht: bool | Unset = UNSET
    eta: str | Unset = UNSET
    j_speed: str | Unset = UNSET
    route: list[RoutePart] | Unset = UNSET
    wht: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ar: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ar, Unset):
            ar = []
            for ar_item_data in self.ar:
                ar_item = ar_item_data.to_dict()
                ar.append(ar_item)

        cht = self.cht

        dist_m = self.dist_m

        dist_u = self.dist_u

        eht = self.eht

        eta = self.eta

        j_speed = self.j_speed

        route: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.route, Unset):
            route = []
            for route_item_data in self.route:
                route_item = route_item_data.to_dict()
                route.append(route_item)

        wht = self.wht

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ar is not UNSET:
            field_dict["ar"] = ar
        if cht is not UNSET:
            field_dict["cht"] = cht
        if dist_m is not UNSET:
            field_dict["distM"] = dist_m
        if dist_u is not UNSET:
            field_dict["distU"] = dist_u
        if eht is not UNSET:
            field_dict["eht"] = eht
        if eta is not UNSET:
            field_dict["eta"] = eta
        if j_speed is not UNSET:
            field_dict["jSpeed"] = j_speed
        if route is not UNSET:
            field_dict["route"] = route
        if wht is not UNSET:
            field_dict["wht"] = wht

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alternate_route import AlternateRoute
        from ..models.route_part import RoutePart

        d = dict(src_dict)
        _ar = d.pop("ar", UNSET)
        ar: list[AlternateRoute] | Unset = UNSET
        if _ar is not UNSET:
            ar = []
            for ar_item_data in _ar:
                ar_item = AlternateRoute.from_dict(ar_item_data)

                ar.append(ar_item)

        cht = d.pop("cht", UNSET)

        dist_m = d.pop("distM", UNSET)

        dist_u = d.pop("distU", UNSET)

        eht = d.pop("eht", UNSET)

        eta = d.pop("eta", UNSET)

        j_speed = d.pop("jSpeed", UNSET)

        _route = d.pop("route", UNSET)
        route: list[RoutePart] | Unset = UNSET
        if _route is not UNSET:
            route = []
            for route_item_data in _route:
                route_item = RoutePart.from_dict(route_item_data)

                route.append(route_item)

        wht = d.pop("wht", UNSET)

        route_response = cls(
            ar=ar,
            cht=cht,
            dist_m=dist_m,
            dist_u=dist_u,
            eht=eht,
            eta=eta,
            j_speed=j_speed,
            route=route,
            wht=wht,
        )

        route_response.additional_properties = d
        return route_response

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
