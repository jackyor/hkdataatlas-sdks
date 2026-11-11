from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransportationRoute")


@_attrs_define
class TransportationRoute:
    """
    Attributes:
        bound (str | Unset): The direction of the bus route (I - inbound; O - outbound).
        dest_en (str | Unset): The destination of a bus route in English.
        dest_sc (str | Unset): The destination of a bus route in Simplified Chinese.
        dest_tc (str | Unset): The destination of a bus route in Traditional Chinese.
        operator (str | Unset): The operator of the route.
        orig_en (str | Unset): The origin of a bus route in English.
        orig_sc (str | Unset): The origin of a bus route in Simplified Chinese.
        orig_tc (str | Unset): The origin of a bus route in Traditional Chinese.
        route (str | Unset): The bus route number.
        service_type (str | Unset): The service type of the bus route.
    """

    bound: str | Unset = UNSET
    dest_en: str | Unset = UNSET
    dest_sc: str | Unset = UNSET
    dest_tc: str | Unset = UNSET
    operator: str | Unset = UNSET
    orig_en: str | Unset = UNSET
    orig_sc: str | Unset = UNSET
    orig_tc: str | Unset = UNSET
    route: str | Unset = UNSET
    service_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bound = self.bound

        dest_en = self.dest_en

        dest_sc = self.dest_sc

        dest_tc = self.dest_tc

        operator = self.operator

        orig_en = self.orig_en

        orig_sc = self.orig_sc

        orig_tc = self.orig_tc

        route = self.route

        service_type = self.service_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bound is not UNSET:
            field_dict["bound"] = bound
        if dest_en is not UNSET:
            field_dict["dest_en"] = dest_en
        if dest_sc is not UNSET:
            field_dict["dest_sc"] = dest_sc
        if dest_tc is not UNSET:
            field_dict["dest_tc"] = dest_tc
        if operator is not UNSET:
            field_dict["operator"] = operator
        if orig_en is not UNSET:
            field_dict["orig_en"] = orig_en
        if orig_sc is not UNSET:
            field_dict["orig_sc"] = orig_sc
        if orig_tc is not UNSET:
            field_dict["orig_tc"] = orig_tc
        if route is not UNSET:
            field_dict["route"] = route
        if service_type is not UNSET:
            field_dict["service_type"] = service_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bound = d.pop("bound", UNSET)

        dest_en = d.pop("dest_en", UNSET)

        dest_sc = d.pop("dest_sc", UNSET)

        dest_tc = d.pop("dest_tc", UNSET)

        operator = d.pop("operator", UNSET)

        orig_en = d.pop("orig_en", UNSET)

        orig_sc = d.pop("orig_sc", UNSET)

        orig_tc = d.pop("orig_tc", UNSET)

        route = d.pop("route", UNSET)

        service_type = d.pop("service_type", UNSET)

        transportation_route = cls(
            bound=bound,
            dest_en=dest_en,
            dest_sc=dest_sc,
            dest_tc=dest_tc,
            operator=operator,
            orig_en=orig_en,
            orig_sc=orig_sc,
            orig_tc=orig_tc,
            route=route,
            service_type=service_type,
        )

        transportation_route.additional_properties = d
        return transportation_route

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
