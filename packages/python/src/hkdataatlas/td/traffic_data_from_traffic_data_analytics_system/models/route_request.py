from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.route_request_lang import RouteRequestLang, check_route_request_lang
from ..models.route_request_tunnel import RouteRequestTunnel, check_route_request_tunnel
from ..models.route_request_type import RouteRequestType, check_route_request_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteRequest")


@_attrs_define
class RouteRequest:
    """Request for route traffic data.

    Attributes:
        end (Any): Location coordinates and optional buffer distance. Provide either WGS84 latitude and longitude in
            decimal degrees, or HK80 x and y coordinates. Buffer is the maximum distance in metres used to find the closest
            starting or destination edge; if omitted, the system default is 50 metres.
        start (Any): Location coordinates and optional buffer distance. Provide either WGS84 latitude and longitude in
            decimal degrees, or HK80 x and y coordinates. Buffer is the maximum distance in metres used to find the closest
            starting or destination edge; if omitted, the system default is 50 metres.
        depart_in (int | Unset): Optional departure time in minutes from the current time. The latest departure is 90
            minutes from now; if omitted, departure is assumed to be the current time. The documented options are 0, 15, 30,
            45, 60, 75, and 90. Other values are mapped to the closest option and are therefore accepted.
        lang (RouteRequestLang | Unset): Optional response language. If omitted, Traditional Chinese is assumed.
        tunnel (RouteRequestTunnel | Unset): Optional code to force use of a cross-harbour tunnel when crossing between
            Hong Kong Island and Kowloon.
        type_ (RouteRequestType | Unset): Optional route type. If omitted, shortest time is assumed.
    """

    end: Any
    start: Any
    depart_in: int | Unset = UNSET
    lang: RouteRequestLang | Unset = UNSET
    tunnel: RouteRequestTunnel | Unset = UNSET
    type_: RouteRequestType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end: Any
        end = self.end

        start: Any
        start = self.start

        depart_in = self.depart_in

        lang: str | Unset = UNSET
        if not isinstance(self.lang, Unset):
            lang = self.lang

        tunnel: str | Unset = UNSET
        if not isinstance(self.tunnel, Unset):
            tunnel = self.tunnel

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "start": start,
            }
        )
        if depart_in is not UNSET:
            field_dict["departIn"] = depart_in
        if lang is not UNSET:
            field_dict["lang"] = lang
        if tunnel is not UNSET:
            field_dict["tunnel"] = tunnel
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_end(data: object) -> Any:
            return cast(Any, data)

        end = _parse_end(d.pop("end"))

        def _parse_start(data: object) -> Any:
            return cast(Any, data)

        start = _parse_start(d.pop("start"))

        depart_in = d.pop("departIn", UNSET)

        _lang = d.pop("lang", UNSET)
        lang: RouteRequestLang | Unset
        if isinstance(_lang, Unset):
            lang = UNSET
        else:
            lang = check_route_request_lang(_lang)

        _tunnel = d.pop("tunnel", UNSET)
        tunnel: RouteRequestTunnel | Unset
        if isinstance(_tunnel, Unset):
            tunnel = UNSET
        else:
            tunnel = check_route_request_tunnel(_tunnel)

        _type_ = d.pop("type", UNSET)
        type_: RouteRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_route_request_type(_type_)

        route_request = cls(
            end=end,
            start=start,
            depart_in=depart_in,
            lang=lang,
            tunnel=tunnel,
            type_=type_,
        )

        route_request.additional_properties = d
        return route_request

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
